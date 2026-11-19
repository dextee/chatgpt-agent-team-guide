# Verification and limits

[Home](README.md)

## Current verification, 20 November 2026

| Check | Observed result |
|---|---|
| Installation and CLI discovery | On Windows with Codex CLI 0.170.0, a fresh trusted Git project exposed zero guide roles before installation. Preview created no files. Installation produced nine files with matching hashes. Afterward, `codex debug prompt-input` exposed all nine names and descriptions in the spawn tool. Reinstallation skipped all nine. The test used an isolated client home. |
| Filesystem behavior | All four installer tests passed on Windows, including preservation of customized files and rejection of hard-linked files and junction destinations. |
| Documentation and configurations | All twelve validator regressions passed. The validator checked local links and anchors, nine role files and their README rows, 17 PNGs and their manifests, 24 task rows, twelve recipes and the four published example costs. |
| Recorded support example | Eight synthetic tickets matched their expected routes. The checker rejected 16 intentionally invalid answers. A separate answer can be checked with `--output`. Summary meaning still needs comparison with the source ticket. |
| Source and reader review | Three AI reviewers checked the official sources, prompts and reader-facing instructions. Both image API snippets parsed as Python. All 17 illustrations were inspected, including the archived illustration of October's three-model selection. [Audit findings](AUDIT.md) |

The discovery test shows that one local CLI exposed the installed roles for delegation. It did not start a child, run a paid image request or measure task quality. Check model access and tool permissions in the client you intend to use. The support example records a separate October run. [Example and run record](examples/support-triage/README.md)

Run these checks from the repository root with Python 3.11 or later.

```bash
python scripts/test_installer.py
python scripts/test_validation.py
python scripts/check_demo.py
python scripts/validate.py
```

GitHub runs the same commands on Windows and Linux with Python 3.11 and 3.12. Select the commit you want to inspect in the [GitHub Actions history](https://github.com/dextee/chatgpt-agent-team-guide/actions/workflows/validate.yml).

## Historical verification through 11 October 2026

### Local checks

- Installer checks exercise a no-write preview, first install, repeat install, preservation of main configuration, backup of a modified agent, rejection of a non-file collision and rejection of a hard-linked agent before any copying.
- The repository validator checks internal file links and heading anchors, Markdown fences, nine agent definitions, model/effort agreement with the role map and the explicit supported model/effort pairs, every declared PNG asset and its unique filename/hash/dimensions, 24 task rows, twelve workflow recipes and the published cost arithmetic.
- The image manifest records inspection claims for the artwork. Static validation checks those records and bytes; it does not perform a visual inspection. The original nine illustrations were inspected in the September review.
- Product statements were checked against the official pages in [the source register](SOURCES.md).
- Cost regressions alter the displayed total, cross-document rate and row token count to confirm each inconsistency is rejected. The validator reads the actual published tables.
- Technical refresh regressions reject an unsupported Sol effort or unknown model even when the TOML and role map agree, reject duplicate image declarations and missing single-quoted HTML image links, and accept an additional declared 1536 × 768 PNG without a fixed gallery count.

On Linux, the documented commands completed successfully: three installer cases executed and the Windows junction case was skipped; all ten validation regressions passed; the repository validator checked the unchanged nine-image gallery. Final artwork counts are read from the manifest and must pass the same validator after integration.

After integration on 11 October 2026, the validator passed with **21 Markdown files, 161 local links, nine roles, seventeen images, 24 tasks and twelve recipes**. Installer checks and all ten validator regressions passed again; the recorded-example checker matched eight synthetic tickets and rejected seven invalid-output mutations. The eight new images were visually inspected. The temporary rendered preview was checked in a browser at 1440 × 1000 and 390 × 844: all eight README images loaded, no page overflow, the role disclosure opened, and navigation to the recorded example worked. These are local and preview checks; no hosted GitHub Actions result is claimed.

### Independent agent review

Two separate AI subagents reviewed the source claims and all nine original images on 29 September 2026. Their review found a hard-link overwrite risk in the installer and a gap in the cost-table regression check. Both were corrected, with reproductions added to the tests. The image review prompted closer conceptual-art captions, more descriptive alt text and clearer VYR links. See the [audit summary](AUDIT.md).

This is an AI-assisted review with reproducible checks, not a third-party certification or a human security audit.

### Scope of the October checks

The [support-triage demonstration](examples/support-triage/README.md) records one real scoped subagent execution on eight synthetic requests on 11 October 2026. Expected routing was saved first. All eight recorded routes matched those expectations; the parent also reviewed each summary against its input. The offline checker verifies the recorded data and rejects seven deliberately invalid output variants. Re-running that checker does not call a model. This is not a comparative benchmark, a customer accuracy measurement or a discovery test of the nine installed custom-agent files. Exact backend identity and usage were not independently reported; see the [run record](examples/support-triage/run-record.json).

These static and installer checks include no live inference evaluation of the nine recommended roles. They use temporary directories and do not install agents into the owner's active profile. They establish the tested filesystem behavior and configuration consistency, not model entitlement, discovery in every client release or task-quality performance. Any separately recorded task demonstration must state its actual execution method and cannot substitute for custom-agent discovery or a comparative benchmark.

The example API costs use hypothetical fixed token counts. There are no measured speed, quality or savings claims. The evaluation worksheet is empty so users can record their own results.

The image tool did not expose an exact backend model. Generated artwork is credited to the built-in generation method without asserting GPT Image 2.5 provenance.
