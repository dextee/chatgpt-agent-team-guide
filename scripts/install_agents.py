"""Install this guide's agent definitions without replacing main Codex settings."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import os
from pathlib import Path
import shutil
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
        if node.is_symlink() or (hasattr(node, 'is_junction') and node.is_junction()):
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
        if dest.is_symlink() or (dest.exists() and not dest.is_file()):
            raise ValueError(f'Refusing non-regular destination: {dest}')
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
        shutil.copy2(source, dest)
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
