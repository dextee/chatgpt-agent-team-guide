# Your first useful agent task

[Home](../README.md) · [Business guide](business-guide.md) · [Developer setup](../SETUP.md)

You can learn the method with one task and one conversation. Pick a small result you can check against the information you provide.

<img src="../assets/images/guide-team-analogy.png" alt="A lead assigns finding, making and checking, then integrates the returned evidence" width="1000">

## Try this with a short meeting note

Paste this prompt into a conversation. It includes an invented note so you can try it immediately.

```text
Turn the agreed actions in this meeting note into a table.
For each action, return the task, owner and due date. Exclude suggestions.
Use only the note. Write "not stated" when an owner or date is missing.
Include the source sentence so I can check each row.
Do not send messages or make changes in another application.

Meeting note:
Priya will send the revised estimate by Friday.
We agreed the delivery address must be checked.
Sam suggested exploring a second courier next quarter. No decision was made.
```

Expect two rows. Priya owns the estimate and the note gives the deadline as “Friday.” The address check has no named individual or deadline. The second courier was a suggestion, so it should have no action row. Verify that each quoted sentence supports the row beside it.

Try the prompt again with a sanitised note of your own. Keep the source note beside the answer so you can check omissions as well as invented details.

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
