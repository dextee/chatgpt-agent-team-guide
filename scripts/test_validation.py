"""Regression checks for misleading displayed cost examples."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib
from cost_check import check_cost_tables

ROOT = Path(__file__).resolve().parents[1]


class PublishedCostChecks(unittest.TestCase):
    def setUp(self):
        self.example = (ROOT / 'docs/cost-and-evaluation.md').read_text(encoding='utf-8')
        self.models = (ROOT / 'docs/models-and-effort.md').read_text(encoding='utf-8')

    def test_current_documents_reconcile(self):
        self.assertEqual(check_cost_tables(self.example, self.models), [])

    def test_rejects_wrong_displayed_total(self):
        changed = self.example.replace('| $0.002 |', '| $999.000 |')
        self.assertNotEqual(changed, self.example)
        self.assertTrue(any('displayed total' in e for e in check_cost_tables(changed, self.models)))

    def test_rejects_rate_drift_between_documents(self):
        changed = self.models.replace('$0.10 / $0.01 / $0.50', '$0.20 / $0.01 / $0.50')
        self.assertNotEqual(changed, self.models)
        self.assertTrue(any('rates differ' in e for e in check_cost_tables(self.example, changed)))

    def test_rejects_table_tokens_that_disagree_with_prose(self):
        changed = self.example.replace('| Luna | 10,000 /', '| Luna | 20,000 /')
        self.assertNotEqual(changed, self.example)
        self.assertTrue(any('token counts differ' in e for e in check_cost_tables(changed, self.models)))

    def test_rejects_duplicate_model_rate_row(self):
        luna = next(line for line in self.models.splitlines() if line.startswith('| [`gpt-6-luna`]'))
        changed = self.models.replace(luna, luna.replace('$0.10 /', '$999.00 /') + '\n' + luna)
        self.assertTrue(any('unique model-rate rows' in e for e in check_cost_tables(self.example, changed)))


class RepositoryInvariantChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='agent-guide-validation-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'guide'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def validate(self):
        return subprocess.run([sys.executable, 'scripts/validate.py'], cwd=self.root,
                              text=True, capture_output=True,
                              env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))

    def mutate_role(self, field, value):
        path = self.root / 'config/role-map.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        role = next(r for r in data['roles'] if r['name'] == 'guide_implementer')
        agent = self.root / role['file']
        key = 'model_reasoning_effort' if field == 'effort' else field
        original = agent.read_text(encoding='utf-8')
        changed = original.replace(f'{key} = "{role[field]}"', f'{key} = "{value}"')
        self.assertNotEqual(original, changed)
        agent.write_text(changed, encoding='utf-8')
        role[field] = value
        path.write_text(json.dumps(data), encoding='utf-8')

    def test_rejects_unsupported_sol_effort_even_when_role_map_agrees(self):
        self.mutate_role('effort', 'none')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Effort mismatch', result.stderr)

    def test_rejects_unknown_model_even_when_role_map_agrees(self):
        self.mutate_role('model', 'gpt-unverified-model')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Model mismatch', result.stderr)

    def test_accepts_additional_declared_hero_asset(self):
        # A real deterministic PNG fixture exercises a 2:1 asset without relying
        # on a historical fixed gallery count or an image-generation service.
        width, height = 1536, 768
        def chunk(kind, payload):
            return (struct.pack('>I', len(payload)) + kind + payload +
                    struct.pack('>I', zlib.crc32(kind + payload) & 0xffffffff))
        raw = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)) +
               chunk(b'IDAT', zlib.compress((b'\x00' + b'\x20\x40\x60' * width) * height)) + chunk(b'IEND', b''))
        image = self.root / 'assets/images/validation-fixture.png'
        image.write_bytes(raw)
        manifest = self.root / 'assets/image-manifest.json'
        data = json.loads(manifest.read_text(encoding='utf-8'))
        data['images'].append({'file': image.relative_to(self.root).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(),
                               'dimensions': [width, height], 'visually_inspected': True})
        manifest.write_text(json.dumps(data), encoding='utf-8')
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"{len(data['images'])} images", result.stdout)

    def test_rejects_duplicate_declared_asset(self):
        path = self.root / 'assets/image-manifest.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['images'].append(data['images'][0].copy())
        path.write_text(json.dumps(data), encoding='utf-8')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Duplicate illustration content', result.stderr)

    def test_rejects_missing_single_quoted_html_image(self):
        path = self.root / 'README.md'
        path.write_text(path.read_text(encoding='utf-8') + "\n<img src='missing-fixture.png' loading='lazy'>\n", encoding='utf-8')
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Missing link: README.md: missing-fixture.png', result.stderr)


if __name__ == '__main__':
    unittest.main()
