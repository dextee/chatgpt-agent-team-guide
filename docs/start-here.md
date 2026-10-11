# Your first useful agent task

[Home](../README.md) · [Business guide](business-guide.md) · [Developer setup](../SETUP.md)

You can learn the method with one task and one conversation. Pick a small result you can check against the information you provide.

<img src="../assets/images/guide-team-analogy.png" alt="A lead assigns finding, making and checking, then integrates the returned evidence" width="1000">

## Try this with a short meeting note

Use a sanitised note that you are allowed to share. Ask:

```text
Turn this meeting note into an action list.
For each action, return the task, owner and due date.
Use only the note. Write "not stated" when an owner or date is missing.
Include the source sentence so I can check each row.
Do not send messages or make changes in another application.

Meeting note:
[paste your note]
```

Read the returned list alongside the original note. Did it invent a date? Did it mistake a suggestion for a decision? Those checks are more useful than asking whether the answer looks polished.

## Learn three terms

| Term | Everyday meaning |
|---|---|
| **Model** | The engine doing the thinking and generating |
| **Agent** | A worker given instructions, tools and a particular job |
| **Workflow** | The steps and handoffs that produce the result |

A second agent is useful when it can independently examine the result or gather separate evidence. For a short action list, your own review may be sufficient.

## When you add a reviewer

Give it the original note and the action list. Ask it to identify invented details, missing actions and mismatches, with the supporting source sentence. Let the lead resolve the findings and produce the final list.

If your product supports independent agents, confirm that the reviewer actually ran using the activity or execution record. A sentence saying “act as three agents” in an ordinary conversation does not establish independent execution.

## Choose your next step

- [Business owners](business-guide.md): select a recurring task and define a pilot.
- [Developers](../SETUP.md): install and inspect the nine reusable role files.
- [Everyone](task-selector.md): choose a starting model for a concrete task.
- [See an actual run](../examples/support-triage/README.md): compare synthetic inputs with recorded outputs.

Model and tool availability vary by product and account. [Check Chat, Work, Codex and API differences](product-surfaces.md).
