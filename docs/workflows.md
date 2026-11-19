# Twelve workflows with useful handoffs

[Home](../README.md) · [Task selector](task-selector.md) · [Delegation template](../templates/task-brief.md)

Replace the bracketed text and attach the named inputs before copying a recipe. The model and effort beside each recipe are suggested starting points. Choose them in the controls your product exposes. Model names in a prompt cannot change the selected configuration.

In Codex, use the [installed roles](../SETUP.md) and inspect the activity record for each handoff. In a single conversation, do the stages in sequence and label the review a self-check. Name one owner for each file or live record. For external actions, specify the account, record and change you authorize.

**Sol** means GPT-6.2 Sol, **Astra** means GPT-6.2 Astra and **Terra** means GPT-6.1 Terra. Recipes suggesting Luna assume your client offers GPT-6 Luna. If an installed role requests an unavailable model, select a supported alternative in its TOML and try a small task before assigning it work. [Model and product differences](product-surfaces.md)

All illustrations below are conceptual artwork, not screenshots of software or evidence of completed customer work. [Artwork provenance](../assets/README.md).

## 1. Deliver a feature

![An orderly build and review workflow](../assets/images/workflow-coding.png)

**Lead:** Sol / medium. **Team:** explorer, implementer, reviewer; architect only if the design is unresolved.

```text
Build [feature] in [project]. A user should be able to [observable behavior].
Locate the responsible code and tests. If the installed roles are available,
use guide_explorer for discovery, guide_implementer to edit and guide_reviewer
to inspect the diff after the edit. Otherwise perform the stages yourself.
Exercise the user flow, resolve material findings, and return the changed
files, the checks you actually ran and any behavior still unverified.
```

**Done means:** the requested behavior works, existing relevant behavior remains correct and verification covers the actual change. A successful build alone may not demonstrate the user flow.

## 2. Investigate a hard bug

**Lead:** Astra / high. **Team:** bounded evidence investigators if hypotheses are independent.

```text
Investigate [failure] in [component/version]. Expected [behavior]. Observed
[behavior]. Available steps and logs are [steps, log excerpts or file paths].
Reproduce it if possible. Record what you observed and test the explanation
against the evidence. If the cause is established, have one owner apply the
fix. Rerun the original case and the closest regression check. If you cannot
reproduce it, identify the missing observation and label the cause tentative.
```

**Handoff:** the evidence packet must explain why the proposed cause predicts the observed failure. Do not merge speculative patches simply because tests passed elsewhere.

## 3. Produce a research decision brief

![Research sources converge into a central evidence lens](../assets/images/workflow-research.png)

**Lead:** Sol / high; Astra / high for difficult synthesis. **Team:** researchers split by independent question, then editor.

```text
Research [decision] for [audience] as of [date]. Compare [options] on
[criteria]. Consult primary sources and link each material claim to the
page that supports it. Record conflicts and unavailable evidence. If the
client supports delegation, researchers may take separate questions and
guide_editor may edit the combined brief. Recommend an option and name the
assumption most likely to change the decision.
```

**Done means:** decision criteria are covered, important claims have accessible citations and the report distinguishes evidence from inference.

## 4. Draft a client proposal

**Lead:** Sol / medium. **Team:** researcher for substantiation, editor for the final draft.

```text
Create a proposal for [client problem] using [notes or attached file]. State
outcomes, scope, exclusions, delivery stages, dependencies and acceptance
criteria. Use only supported claims. Flag missing commercial facts instead
of inventing prices, testimonials or ROI. Return the editable draft in
[format]. Render it and inspect it when document tools are available.
Identify outstanding commercial decisions and any uninspected pages.
```

**Handoff:** resolve scope and commercial assumptions before the final design pass. Client-facing polish does not prove the commitments are deliverable.

## 5. Reconcile data or invoices

![Matching records align while exceptions remain visible](../assets/images/workflow-data.png)

**Lead:** Sol / high. **Team:** Luna extraction workers for clear fields; Astra if definitions conflict.

```text
Reconcile [source A] and [source B]. Preserve the originals. State the
matching keys and relevant definitions. Separate confirmed matches,
duplicates, missing records and unresolved differences. Recalculate totals
from the underlying records. In the reconciliation table, include references
to the original rows. For each remaining difference, give the known cause
or the specific missing evidence. Preserve missing values as unknown.
```

**Done means:** totals reconcile or differences are explicitly accounted for. A formatted spreadsheet is not the verification result.

## 6. Complete a browser administration task

![Conceptual browser console with a review magnifier and completion symbol](../assets/images/workflow-browser.png)

*Conceptual illustration. The check symbol is part of the artwork; it does not record an actual browser test or product result.*

Use Terra / medium for a visually guided browser task when available. Have one person or agent operate the tab. Astra can help resolve conflicting requirements before a change.

```text
Set [field] on [record] in [account/project] to [value]. Confirm the
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

Use Terra / medium as visual director. Where the image-generation service exposes the model, try GPT-Image-2.6 Flare for concept variations or GPT-Image-2.6 Sunburst for detailed final artwork. [Image workflow](image-workflow.md)

```text
Prepare [assets and dimensions] for [audience/channel], using [approved
copy and references]. Preserve [brand details]. Generate the assets with
the available image tool, inspect them at delivery size, and return the
files. Report the tool and any model identity it displays. If the tool
cannot produce an asset, return its brief and identify the missing file.
```

**Done means:** usable files exist at the referenced paths and have been visually inspected. An image prompt is a brief, not a completed asset.

## 9. Repair a document

**Lead:** Sol / medium. **Team:** one editor; independent review for consequential amounts or clauses.

```text
Correct [document] using [approved facts or marked-up source]. Preserve the original and
maintain the meaning of unaffected content. Resolve ambiguous amounts or
parties before finalizing. Check calculations, references and extracted
text, then render and inspect all affected pages. Return the final files
with a concise explanation of what changed.
```

**Handoff:** give the reviewer the source and correction request as well as the output. Do not invent missing transaction dates or evidence.

## 10. Triage support at scale

Try Luna / low where available for a stable classification policy. Use Sol when a policy decision needs interpretation.

```text
Classify each request in [input] using [routing policy]. Return one draft
per input ID and use exactly the fields in [output schema]. Apply the
policy's fallback and human-review rules for ambiguous cases. If the
policy leaves a case unresolved, flag the case for a decision without
inventing a category. Keep all actions at the draft stage.
```

Try the [eight-ticket example](../examples/support-triage/README.md) for a complete input, policy, schema, and offline check. In that example, an unclear ticket uses category `other`, next step `clarify_request`, and `human_review: true`. For a production pilot, define the allowed error rate and measure on held-out cases.

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
Compare [current model and effort] with [candidate model and effort] on
[representative cases]. Use [acceptance criteria] for both. For each case
record the result, errors, retries, elapsed time and available usage data.
Include review time and failed attempts in the comparison. Leave unknown
costs blank and state what cannot be compared. Keep a cheaper route only
if it clears the quality threshold.
```

**Done means:** the choice is supported by measured completed-task results. [Evaluation worksheet](../templates/evaluation.csv).
