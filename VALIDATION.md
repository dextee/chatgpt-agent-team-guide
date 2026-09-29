# Verification and limits

[Home](README.md)

Verification date: **2026-09-29**.

## Local checks

- Installer checks exercise a no-write preview, first install, repeat install, preservation of main configuration, backup of a modified agent and rejection of a non-file collision before copying.
- The repository validator checks internal file links and heading anchors, Markdown fences, nine agent definitions, model/effort agreement with the role map, nine unique PNG assets and their hashes/dimensions, 24 task rows, twelve workflow recipes and the published cost arithmetic.
- All nine generated illustrations were visually inspected for their intended role in this guide.
- Product statements were checked against the official pages in [the source register](SOURCES.md).

Reproduce the automated checks with Python 3.11+:

```bash
python scripts/test_installer.py
python scripts/validate.py
```

Run these local checks before publishing an update. No hosted CI workflow is included.

## What these checks do not establish

No live inference evaluation was run for the nine recommended roles. The installer checks use temporary directories and do not install agents into the owner's active profile. They prove filesystem behavior and configuration consistency, not model entitlement, discovery in every client release or task-quality performance.

The example API costs use hypothetical fixed token counts. There are no measured speed, quality or savings claims. The evaluation worksheet is empty so users can record their own results.

The image tool did not expose an exact backend model. Generated artwork is credited to the built-in generation method without asserting GPT Image 2.5 provenance.
