# Pick a model for the task

[Home](../README.md) · [Models and effort](models-and-effort.md) · [Workflow prompts](workflows.md)

These **24 recommendations are our working defaults**, inferred from documented model positioning and practical task structure. They are not OpenAI benchmark rankings. Effort is a starting value, not a universal optimum. For a tiny task, run one agent.

| # | Task | Start with | Escalate when | Evidence of completion |
|---|---|---|---|---|
| 1 | Extract fields from a clean document | Luna / low | Layout or meaning is ambiguous: Sol / medium | Fields reconcile to source pages |
| 2 | Classify support requests | Luna / low | Categories overlap or consequences rise: Sol / medium | Held-out examples meet the error target |
| 3 | Find files and symbols | Luna / high | Execution crosses many systems: Sol / high | Exact paths and call relationships |
| 4 | Apply a mechanical edit | Luna / medium | Behavior changes: Sol / medium | Intended diff, no unrelated edits |
| 5 | Summarize a meeting | Luna / medium | Conflicting decisions: Sol / medium | Actions, owners and dates trace to notes |
| 6 | Everyday feature implementation | Sol / medium | Architecture is unresolved: Astra / high | Acceptance checks and relevant tests |
| 7 | Small reproduced bug | Sol / medium | Multiple plausible causes persist: Astra / high | Failing case now succeeds |
| 8 | Production incident diagnosis | Astra / high | Missing evidence: gather it before more reasoning | Causal explanation plus recovery evidence |
| 9 | Architecture or migration plan | Astra / high | Constraints conflict: clarify the decision | Dependencies, tradeoffs and rollback plan |
| 10 | Large mechanical refactor | Sol / high | Semantic changes emerge: Astra / high | Scoped diffs and regression coverage |
| 11 | Routine code review | Sol / high | Cross-system consequences: Astra / high | Findings have locations and repro steps |
| 12 | Security-sensitive change review | Astra / high | Specialist domain evidence is missing | Threat assumptions and validated findings |
| 13 | Research a narrow factual question | Sol / medium | Sources disagree: Sol / high | Current primary-source support |
| 14 | Synthesize a difficult research question | Astra / high | New evidence changes the decision | Claim ledger and uncertainty statement |
| 15 | Compare products or vendors | Sol / high | Irreversible or complex choice: Astra / high | Dated evidence and explicit criteria |
| 16 | Draft a client proposal | Sol / medium | Scope or delivery model is unclear: Astra / high | Claims, scope, costs and next step align |
| 17 | Edit an executive report | Sol / medium | Analysis must be rebuilt: Sol / high | Clear narrative; facts match sources |
| 18 | Reconcile spreadsheets or invoices | Sol / high | Definitions or exceptions conflict: Astra / high | Totals reconcile and exceptions are listed |
| 19 | Diagnose a metric change | Sol / high | Several causal explanations compete: Astra / high | Reproducible calculations and caveats |
| 20 | Complete a familiar browser checklist | Sol / medium | Workflow is ambiguous: Astra / high | Saved result verified after reload |
| 21 | Repair or reformat a document | Sol / medium | Financial meaning is unclear: resolve it first | Source fidelity and rendered-page inspection |
| 22 | Generate visual concepts | Image 2.5 Flare | Fine detail or consistency matters: Sunburst | Images fit the brief and intended crop |
| 23 | Refine a final image or precise edit | Image 2.5 Sunburst | Unclear art direction: clarify the brief | Required details preserved visually |
| 24 | Run a frequent bounded automation | Luna / medium | Exception rate grows: Sol / medium | Evaluation pass rate and per-task usage |

Image models do not take the reasoning-effort setting used by the text models. Select image quality separately. A Sol visual director can prepare the brief and judge the result; the image tool creates the bitmap.

## Route by what makes the work difficult

1. **Unclear result:** resolve requirements before dispatching workers.
2. **Clear result, repetitive work:** begin with Luna and an objective check.
3. **Several steps and judgment:** begin with Sol.
4. **Ambiguity, hard tradeoffs or deep reasoning:** use Astra for the decision or the whole task.
5. **Missing permissions or inaccessible evidence:** fix access or obtain the evidence. A model upgrade does not supply it.

An ordinary Chat session may not offer these model choices or real subagents. Use the [product guide](product-surfaces.md) before following the installation instructions.

Basis: [official model selection](https://developers.openai.com/api/docs/guides/model-selection), [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra), [Sol](https://developers.openai.com/api/docs/models/gpt-6-sol), [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), and [image prompting](https://developers.openai.com/api/docs/guides/image-prompting), checked 2026-09-29.
