# Twelve workflows with useful handoffs

[Home](../README.md) · [Task selector](task-selector.md) · [Delegation template](../templates/task-brief.md)

These recipes are editorial starting points. They use [the installable roles](../SETUP.md). In Work, request equivalent roles using available models and tools; verify actual routing. In Chat without subagents, run the stages sequentially.

## 1. Deliver a feature

![An orderly build and review workflow](../assets/images/workflow-coding.png)

**Lead:** Sol / medium. **Team:** explorer, implementer, reviewer; architect only if the design is unresolved.

```text
Build [feature] in this project. Success means [observable behavior].
Have guide_explorer locate the responsible files and existing tests.
Use guide_implementer to make the change, then guide_reviewer to inspect
the result independently. Resolve material findings and verify the actual
user flow. Return the changed files, checks performed and remaining limits.
```

**Done means:** the requested behavior works, existing relevant behavior remains correct and verification covers the actual change. A successful build alone may not demonstrate the user flow.

## 2. Investigate a hard bug

**Lead:** Astra / high. **Team:** bounded evidence investigators if hypotheses are independent.

```text
Investigate [failure]. Here are the reproduction steps and observed logs.
Separate observations from hypotheses. Delegate independent evidence
questions, then choose the explanation supported by the results. Have one
agent own the fix. Prove the reproduction no longer fails and check the
closest regression risk. Preserve any rollback needed for this change.
```

**Handoff:** the evidence packet must explain why the proposed cause predicts the observed failure. Do not merge speculative patches simply because tests passed elsewhere.

## 3. Produce a research decision brief

![Research sources converge into a central evidence lens](../assets/images/workflow-research.png)

**Lead:** Sol / high; Astra / high for difficult synthesis. **Team:** researchers split by independent question, then editor.

```text
Research [decision] for [audience]. Evaluate [criteria] using current
primary sources. Divide independent questions among researchers. Record
publication dates, evidence, uncertainty and conflicting claims. Reconcile
the findings before guide_editor writes the brief. Give a recommendation,
the strongest alternative and the evidence that could change the choice.
```

**Done means:** decision criteria are covered, important claims have accessible citations and the report distinguishes evidence from inference.

## 4. Draft a client proposal

**Lead:** Sol / medium. **Team:** researcher for substantiation, editor for the final draft.

```text
Create a proposal for [client problem] using the supplied notes. State
outcomes, scope, exclusions, delivery stages, dependencies and acceptance
criteria. Use only supported claims. Flag missing commercial facts instead
of inventing prices, testimonials or ROI. Provide an editable draft and
check the rendered document before delivery.
```

**Handoff:** resolve scope and commercial assumptions before the final design pass. Client-facing polish does not prove the commitments are deliverable.

## 5. Reconcile data or invoices

![Matching records align while exceptions remain visible](../assets/images/workflow-data.png)

**Lead:** Sol / high. **Team:** Luna extraction workers for clear fields; Astra if definitions conflict.

```text
Reconcile [source A] and [source B]. Preserve the originals. State the
matching keys and relevant definitions. Separate confirmed matches,
duplicates, missing records and unresolved differences. Recalculate totals
from the underlying records. Produce a reconciliation table and explain
every remaining difference without treating missing data as zero.
```

**Done means:** totals reconcile or differences are explicitly accounted for. A formatted spreadsheet is not the verification result.

## 6. Complete a browser administration task

![A precise browser operations console](../assets/images/workflow-browser.png)

**Lead:** Sol / medium; Astra / high for an unfamiliar or ambiguous workflow. **Team:** one browser operator.

```text
Complete [specific authorized change] in [account/project]. Confirm the
target identity before editing. Use the approved browser session. After
saving, reopen or reload the final object and verify the exact values.
Report completion only for the state actually observed. Stop dependent
work if a tool permission or required account access is unavailable.
```

**Ownership:** keep one agent on the live browser tab. Independent agents can review documentation or acceptance criteria without competing for the same UI state.

## 7. Refactor several modules

**Lead:** Sol / high. **Team:** architect defines boundaries, implementers own disjoint files, reviewer checks integration.

```text
Refactor [area] while preserving [public behavior]. Establish the base
revision and acceptance checks. Partition independent work with explicit
file ownership. Assign shared interfaces and integration to one owner.
Review the combined diff and verify cross-module behavior after integration.
```

**Done means:** the merged state satisfies the contract. Separate branch checks cannot establish that the integrated result works.

## 8. Build a visual campaign

![A coordinated creative studio with image variations](../assets/images/workflow-creative.png)

**Lead:** Sol visual director. **Image work:** Flare for exploration; Sunburst for demanding finals when explicitly selectable.

```text
Create a coherent visual package for [audience/channel]. First define the
message, composition, dimensions and invariants. Generate genuinely useful
variants, choose a direction, and refine it. Check copy, brand details,
crop, legibility and consistency. Save every final asset into the project
and record the generation method accurately.
```

**Done means:** usable files exist at the referenced paths and have been visually inspected. An image prompt is a brief, not a completed asset.

## 9. Repair a document

**Lead:** Sol / medium. **Team:** one editor; independent review for consequential amounts or clauses.

```text
Correct [document] using the supplied facts. Preserve the original and
maintain the meaning of unaffected content. Resolve ambiguous amounts or
parties before finalizing. Check calculations, references and extracted
text, then render and inspect all affected pages. Return the final files
with a concise explanation of what changed.
```

**Handoff:** give the reviewer the source and correction request as well as the output. Do not invent missing transaction dates or evidence.

## 10. Triage support at scale

**Lead:** Luna / low for a stable classification task. **Escalation:** Sol for ambiguity.

```text
Classify each request into the provided categories and return the required
schema. Use the uncertain category when the evidence does not support a
choice. Include a short supporting excerpt. Route exceptions for review;
do not send customer replies as part of classification.
```

**Done means:** representative held-out examples meet the agreed precision and exception targets. Do not use training examples as your only evaluation.

## 11. Audit a repository before release

![Independent review inspects a completed artifact](../assets/images/workflow-review.png)

**Lead:** Sol / high. **Team:** independent reviewers by risk; Astra auditor for difficult release decisions.

```text
Review [revision] against [requirements]. Divide independent concerns
among reviewers. Return only material findings supported by a location,
reproduction or missing required evidence. Reconcile overlaps. Verify the
actual candidate revision after fixes and state which checks were not run.
```

**Done means:** requirements have evidence at the candidate revision. “No issues found” is not equivalent to full coverage.

## 12. Reduce the cost of a recurring workflow

**Lead:** Sol / medium for evaluation design. **Candidate worker:** Luna / medium.

```text
Compare [current route] with [candidate route] on the same representative
cases. Define acceptance before running. Record failures, rework, latency,
tool charges and token usage. Keep the cheaper route only if it meets the
quality threshold. Define exceptions that route to a stronger model.
```

**Done means:** the choice is supported by measured completed-task results. [Evaluation worksheet](../templates/evaluation.csv).
