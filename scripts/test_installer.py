"""Filesystem regression checks; no model requests or real profile edits."""
import contextlib
import importlib.util
import io
import os
import subprocess
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('installer', HERE / 'install_agents.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerChecks(unittest.TestCase):
    def test_preview_install_repeat_and_backup(self):
        with tempfile.TemporaryDirectory(prefix='agent-guide-test-') as tmp:
            codex = Path(tmp) / '.codex'
            with contextlib.redirect_stdout(io.StringIO()):
                counts = installer.install(codex, True)
                self.assertEqual(counts['add'], 9)
                self.assertFalse(codex.exists())
                codex.mkdir()
                config = codex / 'config.toml'
                config.write_text('model = "my-existing-model"\n', encoding='utf-8')
                existing_config = config.read_bytes()
                installer.install(codex, False)
                self.assertEqual(len(list((codex / 'agents').glob('*.toml'))), 9)
                self.assertEqual(config.read_bytes(), existing_config)
                self.assertEqual(installer.install(codex, False)['skip'], 9)
                target = codex / 'agents' / 'guide_worker.toml'
                custom = target.read_bytes() + b'\n# local customization\n'
                target.write_bytes(custom)
                self.assertEqual(installer.install(codex, True)['replace'], 1)
                self.assertEqual(target.read_bytes(), custom)
                self.assertFalse((codex / 'agent-team-backups').exists())
                self.assertEqual(installer.install(codex, False)['replace'], 1)
                backups = list((codex / 'agent-team-backups').glob('*/guide_worker.toml'))
                self.assertEqual(len(backups), 1)
                self.assertEqual(backups[0].read_bytes(), custom)
                self.assertEqual(config.read_bytes(), existing_config)

    def test_non_file_collision_stops_before_any_copy(self):
        with tempfile.TemporaryDirectory(prefix='agent-guide-test-') as tmp:
            codex = Path(tmp) / '.codex'
            collision = codex / 'agents' / 'guide_worker.toml'
            collision.mkdir(parents=True)
            with self.assertRaises(ValueError):
                installer.install(codex, False)
            self.assertEqual(list((codex / 'agents').iterdir()), [collision])

    def test_hard_link_stops_before_copy_and_preserves_configuration(self):
        with tempfile.TemporaryDirectory(prefix='agent-guide-test-') as tmp:
            codex = Path(tmp) / '.codex'
            target = codex / 'agents'
            target.mkdir(parents=True)
            config = codex / 'config.toml'
            original = b'model = "existing-model"\n'
            config.write_bytes(original)
            collision = target / 'guide_worker.toml'
            os.link(config, collision)
            for dry_run in (True, False):
                with self.assertRaisesRegex(ValueError, 'hard-linked'):
                    installer.install(codex, dry_run)
                self.assertEqual(config.read_bytes(), original)
                self.assertEqual(collision.read_bytes(), original)
                self.assertEqual(list(target.iterdir()), [collision])
                self.assertFalse((codex / 'agent-team-backups').exists())

    @unittest.skipUnless(os.name == 'nt', 'Windows junction regression')
    def test_junction_destination_preserves_link_target(self):
        with tempfile.TemporaryDirectory(prefix='agent-guide-test-') as tmp:
            base = Path(tmp)
            actual = base / 'actual'
            actual.mkdir()
            marker = actual / 'preserve.txt'
            marker.write_bytes(b'original')
            codex = base / '.codex'
            codex.mkdir()
            junction = codex / 'agents'
            subprocess.run(['cmd', '/c', 'mklink', '/J', str(junction), str(actual)],
                           check=True, capture_output=True)
            for dry_run in (True, False):
                with self.assertRaisesRegex(ValueError, 'linked destination'):
                    installer.install(codex, dry_run)
                self.assertEqual(marker.read_bytes(), b'original')
                self.assertEqual(list(actual.iterdir()), [marker])


if __name__ == '__main__':
    unittest.main()
