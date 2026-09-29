"""Check the published guide's links, model routing and generated assets."""
from pathlib import Path
from decimal import Decimal
import hashlib
import json
import re
import struct
import tomllib
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
links = 0
models = {'gpt-6-astra', 'gpt-6-sol', 'gpt-6-luna'}
efforts = {'low', 'medium', 'high', 'xhigh', 'max'}


def require(condition, message):
    if not condition:
        errors.append(message)


def headings(path):
    result = set()
    counts = {}
    for title in re.findall(r'^#{1,6}\s+(.+)$', path.read_text(encoding='utf-8'), re.M):
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        result.add(slug if n == 0 else f'{slug}-{n}')
    return result


markdown = sorted(ROOT.rglob('*.md'))
for path in markdown:
    content = path.read_text(encoding='utf-8')
    require(content.count('```') % 2 == 0, f'Unclosed fence: {path.name}')
    visible = re.sub(r'```.*?```', '', content, flags=re.S)
    targets = re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', visible)
    targets += re.findall(r'(?:src|href)="([^"]+)"', visible)
    for target in targets:
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        links += 1
        dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        require(dest.is_relative_to(ROOT), f'Link escapes repository: {path.name}: {target}')
        require(dest.exists(), f'Missing link: {path.name}: {target}')
        if dest.exists() and dest.suffix == '.md' and parsed.fragment:
            require(unquote(parsed.fragment) in headings(dest), f'Missing heading: {path.name}: {target}')

roles = json.loads((ROOT/'config/role-map.json').read_text(encoding='utf-8'))['roles']
require(len(roles) == 9, 'Expected nine roles')
require(len({r['name'] for r in roles}) == 9, 'Duplicate role names')
for role in roles:
    data = tomllib.loads((ROOT/role['file']).read_text(encoding='utf-8'))
    for key in ('name', 'description', 'developer_instructions'):
        require(bool(data.get(key)), f'Missing agent field: {role["name"]}/{key}')
    require(data['name'] == role['name'], f'Role name mismatch: {role}')
    require(data['model'] == role['model'] and data['model'] in models, f'Model mismatch: {role}')
    require(data['model_reasoning_effort'] == role['effort'] and role['effort'] in efforts, f'Effort mismatch: {role}')
for path in ROOT.rglob('*.toml'):
    tomllib.loads(path.read_text(encoding='utf-8'))

assets = json.loads((ROOT/'assets/image-manifest.json').read_text(encoding='utf-8'))
require(assets['exact_backend_model'] is None, 'Unsupported image model provenance')
require(len(assets['images']) == 9, 'Expected nine illustrations')
require(len({a['sha256'] for a in assets['images']}) == 9, 'Duplicate illustration content')
for item in assets['images']:
    path = ROOT / item['file']
    raw = path.read_bytes()
    require(raw[:8] == b'\x89PNG\r\n\x1a\n', f'Invalid PNG: {path.name}')
    width, height = struct.unpack('>II', raw[16:24])
    require([width, height] == item['dimensions'], f'Image dimensions mismatch: {path.name}')
    require(width >= 1000 and height >= 700, f'Image resolution too small: {path.name}')
    require(hashlib.sha256(raw).hexdigest() == item['sha256'], f'Image hash mismatch: {path.name}')
    require(item['visually_inspected'] is True, f'Image not inspected: {path.name}')

selector = (ROOT/'docs/task-selector.md').read_text(encoding='utf-8')
require(len(re.findall(r'^\| \d+ \|', selector, re.M)) == 24, 'Expected 24 task recommendations')
recipes = (ROOT/'docs/workflows.md').read_text(encoding='utf-8')
require(len(re.findall(r'^## \d+\.', recipes, re.M)) == 12, 'Expected 12 workflows')
for inp, out, expected in [('0.1','0.5','0.002'),('2','10','0.040'),('10','50','0.200')]:
    actual = Decimal('0.01')*Decimal(inp) + Decimal('0.002')*Decimal(out)
    require(actual == Decimal(expected), f'Cost arithmetic mismatch: {actual}')

for path in ROOT.rglob('*'):
    if not path.is_file() or '.git' in path.parts or '__pycache__' in path.parts:
        continue
    if path.suffix in {'.md', '.py', '.json', '.toml', '.csv', '.yml', '.yaml'}:
        value = path.read_text(encoding='utf-8')
        require(not re.search(r'(?:ghp_|gho_|sk-proj-)[A-Za-z0-9_-]{20,}', value), f'Credential-like content: {path.name}')
        require('C:\\Users\\Privacy' not in value, f'Local private path: {path.name}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(markdown)} Markdown files; {links} local links; 9 roles; 9 images; 24 tasks; 12 workflows; cost arithmetic; content checks.')
