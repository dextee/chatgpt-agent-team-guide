# A small example you can inspect

[Guide home](../../README.md) · [Business guide](../../docs/business-guide.md)

**Synthetic support triage, recorded on 11 October 2026.** One scoped subagent read eight invented requests and returned structured drafts. Expectations were saved before the run. The requested model was `gpt-6-luna` / high; the runtime did not expose a separate backend model identity. This is a teaching example, not a model benchmark or a customer system.

<img src="../../assets/images/guide-business-example.png" alt="Synthetic support messages enter a classification desk, with one unclear request held for human clarification" width="900">

*Illustration of the method. The inspectable JSON below records the result.*

## Follow a request through the work

| Source request | Recorded category | Proposed next step | Policy escalation |
|---|---|---|---|
| T01: move an appointment | booking | prepare booking options | Routine draft |
| T02: cannot sign in, urgent | access | investigate access | Human review |
| T03: charged twice | billing | review billing | Human review |
| T07: “I need help with it.” | other | ask for clarification | Human review |

The review flag marks the cases this policy escalates. **Every result remains a draft.** A booking label does not confirm availability; a billing label does not authorize a refund. There is no sending or account-changing step in this example.

For T07, the recorded result is:

```json
{
  "id": "T07",
  "category": "other",
  "next_step": "clarify_request",
  "human_review": true,
  "status": "draft",
  "source_id": "T07",
  "summary": "Requests help without specifying what is needed."
}
```

The useful behavior is preserving the missing information so a person can resolve it.

## Open the evidence

| Artifact | What you can inspect |
|---|---|
| [Input and policy](input.json) | The eight original messages, categories and review rules |
| [Task prompt](prompt.txt) | The reusable, public task instructions |
| [Expectations](expected.json) | The expected category, route and review flag, written before execution |
| [Recorded output](recorded-output.json) | The actual structured drafts returned in the editing session |
| [Run record](run-record.json) | Date, requested configuration, parent review and limitations |
| [Offline checker](../../scripts/check_demo.py) | The checks and deliberately invalid outputs they reject |

From the repository root, with Python 3.11+:

```bash
python scripts/check_demo.py
```

This rechecks the **recorded** output offline. It does not call a model. To make a fresh run, provide [input.json](input.json) and [prompt.txt](prompt.txt) to your available model, save its returned JSON separately, and compare it with the expectations before accepting it. Record the model identity your client actually reports and any failures.

## What this establishes

All eight recorded items match this fixture's category, route and escalation expectations. The checker also rejects wrong routes, wrong source references, an approved status, missing billing review, missing items and duplicates. The guide's maintainer compared all eight summaries with the source messages.

The result does not establish production accuracy, independent reviewer performance, savings, latency, or discovery of the nine installed custom agents. Real support work needs representative cases, access controls, approved knowledge, human action boundaries and ongoing evaluation.
