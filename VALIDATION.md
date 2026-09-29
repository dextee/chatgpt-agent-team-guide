# Verification and limits

[Home](README.md)

Verification date: **2026-09-29**.

## Local checks

- Installer checks exercise a no-write preview, first install, repeat install, preservation of main configuration, backup of a modified agent, rejection of a non-file collision and rejection of a hard-linked agent before any copying.
- The repository validator checks internal file links and heading anchors, Markdown fences, nine agent definitions, model/effort agreement with the role map, nine unique PNG assets and their hashes/dimensions, 24 task rows, twelve workflow recipes and the published cost arithmetic.
- All nine generated illustrations were visually inspected for their intended role in this guide.
- Product statements were checked against the official pages in [the source register](SOURCES.md).
- Cost regressions alter the displayed total, cross-document rate and row token count to confirm each inconsistency is rejected. The validator reads the actual published tables.

## Independent agent review

Two separate AI subagents reviewed the source claims and all nine original images on 29 September 2026. Their review found a hard-link overwrite risk in the installer and a gap in the cost-table regression check. Both were corrected, with reproductions added to the tests. The image review prompted closer conceptual-art captions, more descriptive alt text and clearer VYR links. See the [audit summary](AUDIT.md).

This is an AI-assisted review with reproducible checks, not a third-party certification or a human security audit.

Reproduce the automated checks with Python 3.11+:

```bash
python scripts/test_installer.py
python scripts/test_validation.py
python scripts/validate.py
```

Run these local checks before publishing an update. No hosted CI workflow is included.

## What these checks do not establish

No live inference evaluation was run for the nine recommended roles. The installer checks use temporary directories and do not install agents into the owner's active profile. They prove filesystem behavior and configuration consistency, not model entitlement, discovery in every client release or task-quality performance.

The example API costs use hypothetical fixed token counts. There are no measured speed, quality or savings claims. The evaluation worksheet is empty so users can record their own results.

The image tool did not expose an exact backend model. Generated artwork is credited to the built-in generation method without asserting GPT Image 2.5 provenance.
