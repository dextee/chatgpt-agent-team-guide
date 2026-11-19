# Pick a model for the task

[Home](../README.md) · [Models and effort](models-and-effort.md) · [Workflow prompts](workflows.md)

Pick one row, run its check on a representative case, then decide whether to change the model or effort. These 24 task assignments are the guide's editorial recommendations.

**Sol** means GPT-6.2 Sol, **Astra** means GPT-6.2 Astra and **Terra** means GPT-6.1 Terra. Use **Luna** (GPT-6 Luna) only when your product lists it and a representative task succeeds with the selected effort. If Luna is unavailable, start those rows with Sol / low. For a visual task, check that both the model and the required browser, image or file tool are available. [Model IDs and reasoning effort](models-and-effort.md)

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
| 17 | Edit an executive report | Sol / medium | Analysis needs rebuilding → Sol / high | Key facts match the cited sources |
| 18 | Reconcile spreadsheets or invoices | Sol / high | Definitions or exceptions conflict: Astra / high | Totals reconcile and exceptions are listed |
| 19 | Diagnose a metric change | Sol / high | Several causal explanations compete: Astra / high | Reproducible calculations and caveats |
| 20 | Complete a familiar browser checklist | Terra / medium with browser access | Several rules must be reconciled → ask Astra to resolve them before the operator acts | Correct record and saved values verified after reopening |
| 21 | Repair or reformat a document | Sol / medium to edit | Page layout needs a visual check → Terra / medium with rendered pages | Corrected text matches the source and fits on the page |
| 22 | Generate visual concepts | GPT-Image-2.6 Flare where selectable | A final concept needs fine detail → Sunburst | Exported images fit the brief and intended crop |
| 23 | Refine a final image or precise edit | GPT-Image-2.6 Sunburst where selectable | The intended change is unclear → specify the edit and what to preserve | Inspect the actual output beside the source image |
| 24 | Run a frequent bounded automation | Luna / medium | Exception rate grows: Sol / medium | Evaluation pass rate and per-task usage |

The visual director can use Terra to inspect source images and review the finished work. The image generation tool produces the asset. If your tool hides the image model, record the tool name and leave the model identity unknown. [Image workflow](image-workflow.md)

## Route by what makes the work difficult

1. Resolve unclear requirements before assigning work.
2. For a repeatable task, test a light setting against explicit acceptance criteria.
3. Start with Sol for multistep work that requires judgment.
4. Use Astra for decisions with competing constraints. Give it the evidence that bears on the decision.
5. Try Terra for visual interpretation or screen navigation when your client exposes the required tools.

An ordinary Chat session may not offer these model choices or real subagents. Use the [product guide](product-surfaces.md) before following the installation instructions.

The model families and image options were checked on 20 November 2026. [OpenAI model selection](https://developers.openai.com/api/docs/guides/model-selection) · [OpenAI image generation](https://developers.openai.com/api/docs/guides/image-generation)
