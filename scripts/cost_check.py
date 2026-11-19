"""Reconcile the rendered cost example with its token counts and model-rate table."""
from decimal import Decimal
import re

MODEL_NAMES = {
    'gpt-6-luna': 'Luna',
    'gpt-6.1-terra': 'Terra',
    'gpt-6.2-sol': 'Sol',
    'gpt-6.2-astra': 'Astra',
}


def check_cost_tables(example: str, models: str) -> list[str]:
    errors = []
    counts = re.search(r'\*\*([\d,]+) uncached input tokens and ([\d,]+) billable output tokens\*\*', example)
    if not counts:
        return ['Missing example token counts']
    expected_counts = tuple(int(x.replace(',', '')) for x in counts.groups())
    rates = {}
    source_rows = re.findall(
        r'^\| \[`([\w.-]+)`\]\([^\n]+?\) \| \$([\d.]+) / \$([\d.]+) / \$([\d.]+) \|', models, re.M
    )
    if len(source_rows) != len(MODEL_NAMES) or {r[0] for r in source_rows} != MODEL_NAMES.keys():
        errors.append('Expected unique model-rate rows for all four models')
    for model, inp, cached, out in source_rows:
        if model in MODEL_NAMES:
            rates[MODEL_NAMES[model]] = (Decimal(inp), Decimal(out))
    rows = re.findall(
        r'^\| (\w+) \| ([\d,]+) / 1M × \$([\d.]+) \| ([\d,]+) / 1M × \$([\d.]+) \| \$([\d.]+) \|$', example, re.M
    )
    if len(rows) != len(MODEL_NAMES) or {r[0] for r in rows} != set(MODEL_NAMES.values()):
        errors.append('Expected one complete displayed cost row for each model')
    for model, ins, inp, outs, outp, total in rows:
        tokens = (int(ins.replace(',', '')), int(outs.replace(',', '')))
        row_rates = (Decimal(inp), Decimal(outp))
        if tokens != expected_counts:
            errors.append(f'{model}: table token counts differ from the example text')
        if rates.get(model) != row_rates:
            errors.append(f'{model}: example rates differ from the model guide')
        actual = (tokens[0] * row_rates[0] + tokens[1] * row_rates[1]) / Decimal(1_000_000)
        if actual != Decimal(total):
            errors.append(f'{model}: displayed total {total} should be {actual}')
    return errors
