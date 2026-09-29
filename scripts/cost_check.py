"""Reconcile the rendered cost example with its token counts and model-rate table."""
from decimal import Decimal
import re


def check_cost_tables(example: str, models: str) -> list[str]:
    errors = []
    counts = re.search(r'\*\*([\d,]+) uncached input tokens and ([\d,]+) billable output tokens\*\*', example)
    if not counts:
        return ['Missing example token counts']
    expected_counts = tuple(int(x.replace(',', '')) for x in counts.groups())
    rates = {}
    source_rows = re.findall(
        r'^\| \[`gpt-6-(luna|sol|astra)`\]\([^\n]+?\) \| \$([\d.]+) / \$([\d.]+) / \$([\d.]+) \|', models, re.M
    )
    if len(source_rows) != 3 or len({r[0] for r in source_rows}) != 3:
        errors.append('Expected exactly three unique model-rate rows')
    for model, inp, cached, out in source_rows:
        rates[model] = (Decimal(inp), Decimal(out))
    rows = re.findall(
        r'^\| (Luna|Sol|Astra) \| ([\d,]+) / 1M × \$([\d.]+) \| ([\d,]+) / 1M × \$([\d.]+) \| \$([\d.]+) \|$', example, re.M
    )
    if len(rows) != 3 or {r[0].lower() for r in rows} != {'luna', 'sol', 'astra'}:
        errors.append('Expected one complete displayed cost row for each model')
    if set(rates) != {'luna', 'sol', 'astra'}:
        errors.append('Missing model-rate rows')
    for model, ins, inp, outs, outp, total in rows:
        tokens = (int(ins.replace(',', '')), int(outs.replace(',', '')))
        row_rates = (Decimal(inp), Decimal(outp))
        if tokens != expected_counts:
            errors.append(f'{model}: table token counts differ from the example text')
        if rates.get(model.lower()) != row_rates:
            errors.append(f'{model}: example rates differ from the model guide')
        actual = (tokens[0] * row_rates[0] + tokens[1] * row_rates[1]) / Decimal(1_000_000)
        if actual != Decimal(total):
            errors.append(f'{model}: displayed total {total} should be {actual}')
    return errors
