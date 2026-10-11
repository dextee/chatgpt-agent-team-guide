# Verification and limits

[Home](README.md)

Technical refresh verification date: **2026-10-11**. The original review and image inspection records below retain their historical dates.

## Local checks

- Installer checks exercise a no-write preview, first install, repeat install, preservation of main configuration, backup of a modified agent, rejection of a non-file collision and rejection of a hard-linked agent before any copying.
- The repository validator checks internal file links and heading anchors, Markdown fences, nine agent definitions, model/effort agreement with the role map and the explicit supported model/effort pairs, every declared PNG asset and its unique filename/hash/dimensions, 24 task rows, twelve workflow recipes and the published cost arithmetic.
- The image manifest records inspection claims for the artwork. Static validation checks those records and bytes; it does not perform a visual inspection. The original nine illustrations were inspected in the September review.
- Product statements were checked against the official pages in [the source register](SOURCES.md).
- Cost regressions alter the displayed total, cross-document rate and row token count to confirm each inconsistency is rejected. The validator reads the actual published tables.
- Technical refresh regressions reject an unsupported Sol effort or unknown model even when the TOML and role map agree, reject duplicate image declarations and missing single-quoted HTML image links, and accept an additional declared 1536 × 768 PNG without a fixed gallery count.

On Linux, the documented commands completed successfully: three installer cases executed and the Windows junction case was skipped; all ten validation regressions passed; the repository validator checked the unchanged nine-image gallery. Final artwork counts are read from the manifest and must pass the same validator after integration.

After integration on 11 October 2026, the validator passed with **21 Markdown files, 161 local links, nine roles, seventeen images, 24 tasks and twelve recipes**. Installer checks and all ten validator regressions passed again; the recorded-example checker matched eight synthetic tickets and rejected seven invalid-output mutations. The eight new images were visually inspected. The temporary rendered preview was checked in a browser at 1440 × 1000 and 390 × 844: all eight README images loaded, no page overflow, the role disclosure opened, and navigation to the recorded example worked. These are local and preview checks; no hosted GitHub Actions result is claimed.

## Independent agent review

Two separate AI subagents reviewed the source claims and all nine original images on 29 September 2026. Their review found a hard-link overwrite risk in the installer and a gap in the cost-table regression check. Both were corrected, with reproductions added to the tests. The image review prompted closer conceptual-art captions, more descriptive alt text and clearer VYR links. See the [audit summary](AUDIT.md).

This is an AI-assisted review with reproducible checks, not a third-party certification or a human security audit.

Reproduce the automated checks with Python 3.11+:

```bash
python scripts/test_installer.py
python scripts/test_validation.py
python scripts/check_demo.py
python scripts/validate.py
```

Run these local checks before publishing an update. The [GitHub Actions workflow](.github/workflows/validate.yml) runs them on Linux and Windows with Python 3.11 and 3.12, so Windows can exercise junction rejection. It uses read-only repository permissions, no secrets and immutable action revisions. The October refresh was tested locally; adding a workflow file does not prove a hosted run passed. CI cannot independently verify changing official documentation or image quality.

## What these checks do not establish

The [support-triage demonstration](examples/support-triage/README.md) records one real scoped subagent execution on eight synthetic requests on 11 October 2026. Expected routing was saved first. All eight recorded routes matched those expectations; the parent also reviewed each summary against its input. The offline checker verifies the recorded data and rejects seven deliberately invalid output variants. Re-running that checker does not call a model. This is not a comparative benchmark, a customer accuracy measurement or a discovery test of the nine installed custom-agent files. Exact backend identity and usage were not independently reported; see the [run record](examples/support-triage/run-record.json).

These static and installer checks include no live inference evaluation of the nine recommended roles. They use temporary directories and do not install agents into the owner's active profile. They establish the tested filesystem behavior and configuration consistency, not model entitlement, discovery in every client release or task-quality performance. Any separately recorded task demonstration must state its actual execution method and cannot substitute for custom-agent discovery or a comparative benchmark.

The example API costs use hypothetical fixed token counts. There are no measured speed, quality or savings claims. The evaluation worksheet is empty so users can record their own results.

The image tool did not expose an exact backend model. Generated artwork is credited to the built-in generation method without asserting GPT Image 2.5 provenance.
