"""Install this guide's agent definitions without replacing main Codex settings."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import os
from pathlib import Path
import shutil
import stat
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def agent_sources() -> list[Path]:
    sources = sorted((ROOT / 'agents').glob('guide_*.toml'))
    if len(sources) != 9:
        raise ValueError(f'Expected nine agent definitions; found {len(sources)}')
    seen = set()
    for source in sources:
        data = tomllib.loads(source.read_text(encoding='utf-8'))
        for key in ('name', 'description', 'developer_instructions', 'model', 'model_reasoning_effort'):
            if not isinstance(data.get(key), str) or not data[key].strip():
                raise ValueError(f'{source.name}: missing {key}')
        if data['name'] != source.stem or data['name'] in seen:
            raise ValueError(f'{source.name}: invalid or duplicate name')
        seen.add(data['name'])
    return sources


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_symlink_chain(path: Path) -> None:
    for node in [path, *path.parents]:
        try:
            info = node.lstat()
        except FileNotFoundError:
            continue
        # lstat file attributes are available on Windows Python 3.11 too;
        # Path.is_junction was only added in 3.12.
        reparse = getattr(info, 'st_file_attributes', 0) & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
        if stat.S_ISLNK(info.st_mode) or reparse:
            raise ValueError(f'Refusing linked destination: {node}')


def install(codex_dir: Path, dry_run: bool) -> dict[str, int]:
    sources = agent_sources()
    codex_dir = codex_dir.expanduser().absolute()
    reject_symlink_chain(codex_dir)
    target = codex_dir / 'agents'
    reject_symlink_chain(target)
    if target.exists() and not target.is_dir():
        raise ValueError(f'Agent destination is not a directory: {target}')
    plan = []
    for source in sources:
        dest = target / source.name
        reject_symlink_chain(dest)
        if dest.is_symlink() or (dest.exists() and not dest.is_file()):
            raise ValueError(f'Refusing non-regular destination: {dest}')
        if dest.exists() and dest.stat().st_nlink > 1:
            raise ValueError(f'Refusing hard-linked destination: {dest}')
        action = 'add' if not dest.exists() else ('skip' if digest(dest) == digest(source) else 'replace')
        plan.append((source, dest, action))
    backup = codex_dir / 'agent-team-backups' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    reject_symlink_chain(backup)
    counts = {'add': 0, 'replace': 0, 'skip': 0}
    print(f'{"PREVIEW" if dry_run else "INSTALL"}: {target}')
    for source, dest, action in plan:
        counts[action] += 1
        print(f'{action.upper():7} {dest.name}')
        if dry_run or action == 'skip':
            continue
        target.mkdir(parents=True, exist_ok=True)
        if action == 'replace':
            backup.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dest, backup / dest.name)
        # Replace the directory entry, rather than writing through an existing
        # file that might also be reachable through another hard link.
        with tempfile.NamedTemporaryFile(dir=target, prefix='.agent-install-', delete=False) as staged:
            staged_path = Path(staged.name)
        try:
            shutil.copy2(source, staged_path)
            if digest(source) != digest(staged_path):
                raise OSError(f'Staged copy verification failed: {dest}')
            os.replace(staged_path, dest)
        finally:
            staged_path.unlink(missing_ok=True)
        if digest(source) != digest(dest):
            raise OSError(f'Copy verification failed: {dest}')
    if counts['replace']:
        print(f'{"Planned backup" if dry_run else "Backup"}: {backup}')
    print('Main configuration, project instructions and login state were not modified.')
    return counts


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument('--project', type=Path, help='Install into this project/.codex/agents')
    scope.add_argument('--user', action='store_true', help='Install into CODEX_HOME or ~/.codex')
    parser.add_argument('--dry-run', action='store_true', help='Print the plan without creating files')
    args = parser.parse_args()
    if args.project:
        project = args.project.expanduser().absolute()
        if not project.is_dir():
            parser.error('--project must name an existing project directory')
        target = project / '.codex'
    else:
        target = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    try:
        install(target, args.dry_run)
    except (ValueError, OSError, tomllib.TOMLDecodeError) as error:
        parser.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
