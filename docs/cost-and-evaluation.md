# Choose by completed-task cost

[Home](../README.md) · [Model rates](models-and-effort.md) · [Evaluation CSV](../templates/evaluation.csv)

The useful comparison is the cost of reaching an acceptable result, including failed attempts and rework. A fast first response can still lead to an expensive workflow.

## A transparent arithmetic example

Suppose one successful text request uses **10,000 uncached input tokens and 2,000 billable output tokens**, with no tools, cache writes, long-context surcharge or other mode premium. Using the Standard rates linked in the [model guide](models-and-effort.md):

| Model | Input calculation | Output calculation | Hypothetical total |
|---|---|---|---|
| Luna | 10,000 / 1M × $0.10 | 2,000 / 1M × $0.50 | $0.002 |
| Sol | 10,000 / 1M × $2.00 | 2,000 / 1M × $10.00 | $0.040 |
| Astra | 10,000 / 1M × $10.00 | 2,000 / 1M × $50.00 | $0.200 |

This is arithmetic, not a benchmark or a promise that models use identical tokens. Include all billed output, including reasoning where applicable, when using real usage reports. Image generation, search and other tools can add charges. Subscription allowance cannot be derived from this table.

## Run a small useful comparison

1. Choose representative easy, typical and difficult cases.
2. Write acceptance checks before seeing the outputs.
3. Run the same evidence and constraints through each candidate route.
4. Record quality, failure type, retries, elapsed time and measured usage.
5. Compare cost per accepted result; retain difficult cases for regression checks.
6. Define when the smaller model must escalate.

The included worksheet is intentionally empty. No performance measurements have been invented for this guide.

## Keep the team efficient

Give workers only the context needed for their task. Ask for a compact evidence-backed return. Parallelize independent work when elapsed time matters, but count every worker's usage. Prefer one agent for short tasks or tightly ordered chains.

A separate review is useful when it can find material errors. If the task is a reversible wording change, repeated committees and large test suites may add little value. Match verification to the remaining risk and stop when the defined checks are satisfied.
