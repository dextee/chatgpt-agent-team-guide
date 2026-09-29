# Review record: 29 September 2026

[Home](README.md) · [Reproduce checks](VALIDATION.md) · [Sources](SOURCES.md) · [Artwork](assets/README.md)

The initial reviewed revision was [`f3b6a50`](https://github.com/dextee/chatgpt-agent-team-guide/tree/f3b6a50ead9bdf574277d18570c6de7ff1210cb8). Two separate AI subagents reviewed factual/configuration claims and artwork independently of the editing agent. Changes in this revision address their findings.

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
