"""Check the support-triage example or a new answer to the same fixture offline."""
import argparse
from pathlib import Path
import copy
import json

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / 'examples' / 'support-triage'


def check(input_data, expected, output):
    errors = []
    if not isinstance(output, dict):
        return ['Output must be a JSON object with fixture_id and results']
    if set(output) != {'fixture_id', 'results'}:
        errors.append('Top-level fields must be exactly fixture_id and results')
    if input_data.get('synthetic') is not True:
        errors.append('Example must be explicitly synthetic')
    if output.get('fixture_id') != input_data.get('fixture_id'):
        errors.append('Output fixture does not match input')
    if expected.get('fixture_id') != input_data.get('fixture_id'):
        errors.append('Expectations fixture does not match input')
    tickets = input_data['tickets']
    wanted = expected['expectations']
    results = output.get('results')
    if not isinstance(results, list):
        return errors + ['results must be a JSON array']
    for index, row in enumerate(results):
        if not isinstance(row, dict) or not isinstance(row.get('id'), str):
            errors.append(f'results[{index}] must be an object with a string id')
    if errors:
        return errors
    ids = [row['id'] for row in tickets]
    observed_ids = [row.get('id') for row in results]
    if len(set(ids)) != len(ids):
        errors.append('Input ids must be unique')
    if len(observed_ids) != len(ids) or set(observed_ids) != set(ids):
        errors.append('Every input id must appear exactly once')
    if len(wanted) != len(ids) or {row['id'] for row in wanted} != set(ids):
        errors.append('Every input needs one expectation')
    expected_by_id = {row['id']: row for row in wanted}
    input_by_id = {row['id']: row for row in tickets}
    allowed_keys = {'id', 'category', 'next_step', 'human_review', 'status', 'source_id', 'summary'}
    for row in results:
        ticket_id = row.get('id')
        if ticket_id not in input_by_id or ticket_id not in expected_by_id:
            continue
        if set(row) != allowed_keys:
            errors.append(f'{ticket_id}: unexpected or missing fields')
        for field in ('category', 'next_step', 'human_review'):
            if row.get(field) != expected_by_id[ticket_id][field]:
                errors.append(f'{ticket_id}: incorrect {field}')
        if type(row.get('human_review')) is not bool:
            errors.append(f'{ticket_id}: review flag must be boolean')
        category = row.get('category')
        if not isinstance(category, str) or category not in input_data['policy']['categories']:
            errors.append(f'{ticket_id}: unknown category')
        elif row.get('next_step') != input_data['policy']['routing'][category]:
            errors.append(f'{ticket_id}: route does not match policy')
        needs_review = category in ('billing', 'other') or input_by_id[ticket_id]['priority'] == 'urgent'
        if row.get('human_review') != needs_review:
            errors.append(f'{ticket_id}: review flag violates policy')
        if row.get('source_id') != ticket_id:
            errors.append(f'{ticket_id}: source reference does not match')
        if row.get('status') != 'draft':
            errors.append(f'{ticket_id}: output must remain a draft')
        summary = row.get('summary')
        if not isinstance(summary, str) or not 1 <= len(summary.split()) <= 20:
            errors.append(f'{ticket_id}: summary length must be 1–20 words')
    return errors


def mutation_checks(source, expected, output):
    mutations = []
    for field, value in [('category', 'billing'), ('next_step', 'send_message'),
                         ('source_id', 'invented'), ('status', 'approved'),
                         ('category', []), ('id', ['T01']), ('human_review', 0),
                         ('summary', ''), ('extra_excerpt', 'unexpected')]:
        changed = copy.deepcopy(output)
        row = next(row for row in changed['results'] if row['id'] == 'T01')
        row[field] = value
        mutations.append((field, changed))
    changed = copy.deepcopy(output)
    billing = next(row for row in changed['results'] if row['id'] == 'T03')
    billing['human_review'] = False
    mutations.append(('billing review removed', changed))
    changed = copy.deepcopy(output)
    changed['results'].pop()
    mutations.append(('missing ticket', changed))
    changed = copy.deepcopy(output)
    changed['results'].append(copy.deepcopy(changed['results'][0]))
    mutations.append(('duplicate ticket', changed))
    mutations.extend([
        ('array instead of answer object', []),
        ('extra envelope field', {**output, 'unrequested': True}),
        ('null results', {**output, 'results': None}),
        ('non-object ticket', {**output, 'results': [None]}),
    ])
    for name, changed in mutations:
        if not check(source, expected, changed):
            raise SystemExit(f'Mutation unexpectedly accepted: {name}')
    return len(mutations)


def unique_fields(pairs):
    obj = {}
    for field, value in pairs:
        if field in obj:
            raise ValueError(f'duplicate JSON field {field!r}')
        obj[field] = value
    return obj


def read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8-sig'), object_pairs_hook=unique_fields)
    except (OSError, ValueError) as exc:
        raise SystemExit(f'{path}: {exc}') from exc


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='check a separate JSON answer for the same eight tickets')
    args = parser.parse_args()
    source = read_json(EXAMPLE / 'input.json')
    expected = read_json(EXAMPLE / 'expected.json')
    output_path = args.output or EXAMPLE / 'recorded-output.json'
    output = read_json(output_path)
    errors = check(source, expected, output)
    if errors:
        raise SystemExit('\n'.join(errors))
    if args.output is None:
        print(f'{mutation_checks(source, expected, output)} invalid-output mutations rejected.')
    print(f'PASS: {output_path.name} matches routing and schema checks for {len(output["results"])} '
          'synthetic tickets. Compare each summary with its source to check meaning.')
