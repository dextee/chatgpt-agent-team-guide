# Guide audit

[Home](README.md) · [Reproduce checks](VALIDATION.md) · [Sources](SOURCES.md) · [Artwork](assets/README.md)

## 20 November 2026

Three AI reviewers divided the work across product documentation, runnable examples and the reader's path through the guide. A second pass checked the integrated instructions against OpenAI's documentation and the repository files. The revision started from `50972e0` on the default branch.

| What a reader could get wrong | Change and evidence |
|---|---|
| Install October's model choices after reading November's advice | Updated the nine profiles, lead defaults, model table and recipes together. Validation compares each README role's model and effort with the installed definition. [Model guide](docs/models-and-effort.md) |
| Rely on a reviewer profile to enforce read-only permissions | Removed ineffectual sandbox entries from every profile. The setup guide shows where to select the parent session's permissions and how to inspect child activity. [Setup](SETUP.md) |
| Use a model listed for the app in an incompatible CLI or IDE | Added the minimum CLI version for GPT-6.2 and instructions to check the intended client's model picker. [Client requirements](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) |
| Budget a new Astra request at its predecessor's rate | Recalculated the same short-context example for all four models. At 10,000 uncached input and 2,000 output tokens, GPT-6.2 Astra totals $0.160. [Arithmetic and assumptions](docs/cost-and-evaluation.md) |
| Ask the support agent to invent a category or add an unrequested field | Aligned the recipe with the fixture. A reader can check a fresh JSON answer against the original expectations, then review the wording alongside the input. [Try the example](examples/support-triage/README.md) |
| Attribute generated art to the model that reviewed it | Distinguished Terra's visual review from generation. The image examples identify the model for each API call, and the gallery retains the historical provenance. [Image workflow](docs/image-workflow.md) |

The reviewers checked the 17 illustrations and the public destinations cited by the guide. The OpenAI Help Center returned HTTP 403 to a scripted request, and its article text and version requirement were verified separately in a web reader. The [source register](SOURCES.md) identifies the pages supporting product claims. The [validation record](VALIDATION.md) gives the reproducible checks and their limits.

## 29 September 2026

The initial reviewed revision was [`f3b6a50`](https://github.com/dextee/chatgpt-agent-team-guide/tree/f3b6a50ead9bdf574277d18570c6de7ff1210cb8). Two separate AI subagents reviewed factual/configuration claims and artwork independently of the editing agent. Changes in that revision addressed their findings.

## Coverage and evidence

| Area | Review performed | Evidence and limits |
|---|---|---|
| Model/product statements | Fresh official documentation review of identifiers, prices, context, reasoning, product surfaces and agent configuration | [Source register](SOURCES.md). Model/effort recommendations are editorial; no comparative inference benchmark was run. |
| Installer | Code inspection and temporary-directory filesystem checks, including the reported hard-link reproduction | [Installer tests](scripts/test_installer.py). No change to the owner’s active agent profile. |
| Displayed costs | Recalculate the actual example table and reconcile its token counts and rates with the adjacent documentation | [Cost checks](scripts/cost_check.py) and [regressions](scripts/test_validation.py). Arithmetic validation does not establish future prices. |
| Nine images | Each original viewed, dimensions and SHA-256 hashes compared with the manifest, placements and captions inspected | [Manifest](assets/image-manifest.json). All retained; conceptual illustrations, not product or customer evidence. Exact generation backend remains unknown. |
| Links and structure | Local file/heading links, TOML fields and routing consistency, task/recipe counts | [Validator](scripts/validate.py). Local link validation does not prove every external service remains available. |

## Findings and corrections

| Finding | Correction | Reproduction check |
|---|---|---|
| An existing agent file hard-linked to another file could overwrite that file | Reject multiply linked destinations before copying; stage and replace files by directory entry | Hard-linked `guide_worker.toml` and `config.toml` remain unchanged in preview and install attempts; no other agent is copied |
| The original validator checked fixed cost numbers instead of the displayed table | Parse published rows, token counts and model rates | A displayed Luna total of `$999.000`, an inconsistent model rate and conflicting token counts are each rejected |
| Current Agent OS and commercial relationship were difficult to discover | Add visible authorship, current VYR links and a separate implementation page | [Work with VYR](WORK_WITH_VYR.md) states the relationship, scope process and service-status boundaries |
| Realistic illustrations could be misread without nearby context | Add concept captions near the hero and browser scene; improve gallery alt text; reduce prominent display widths | Original image bytes and provenance remain unchanged |

## Interpretation

This review improves the guide’s correctness and makes its evidence easier to inspect. It is not a certification, endorsement, penetration test, production deployment test or proof of customer savings. Configuration validity and filesystem tests cannot prove account entitlement, live model routing or task quality. Evaluate those in the intended environment before relying on the agent team.

The review involved AI agents and local checks, not an external accredited auditor. No leads or business outcomes are claimed from publishing these materials.

## Technical refresh: 11 October 2026

This section records a later local technical refresh; it does not change the September review record. Official documentation was reopened to check GPT-6.1 Sol routing, effort support, cached-read rates, product surfaces, native Responses delegation and image model selection. [Current sources](SOURCES.md).

The five Sol custom agents and team defaults now select `gpt-6.1-sol`, preserving their existing role-specific efforts. The unsupported 922,000-input-token statement was removed rather than replaced with another derived limit. The validator now checks explicit model/effort pairs independently of the role map and checks all declared images without requiring the historical nine-image count. Mutation tests exercise invalid settings, duplicate declarations and a missing HTML image link; a valid additional hero-shaped fixture proves the gallery can expand.

The three documented Python commands passed locally on Linux: three installer cases executed with the Windows junction case skipped, ten validation cases passed, and the unchanged gallery passed repository validation. A new CI matrix requests Linux and Windows checks on Python 3.11 and 3.12; its presence is not evidence of a completed hosted run. The checkout and Python setup revisions were resolved against the official `actions/checkout` v7.0.1 and `actions/setup-python` v7.0.0 tag records and pinned by commit.

No live model-quality evaluation or active profile installation is part of this technical record. Example API code was checked as documentation, not executed. Image model IDs in those examples do not establish the backend used for this guide's built-in artwork.
