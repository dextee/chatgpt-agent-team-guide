# Make useful, coherent images

[Home](../README.md) · [Artwork gallery](../assets/README.md)

![A creative studio exploring a coordinated set of visual directions](../assets/images/workflow-creative.png)

## Pick the image tool deliberately

For explicitly selectable API models, OpenAI documents **GPT Image 2.5 Flare** for speed and **GPT Image 2.5 Sunburst** for more demanding image quality and editing. The identifiers are `gpt-image-2.5-flare` and `gpt-image-2.5-sunburst`. They are image models, not the text-model setting of the visual-director agent. [Image generation](https://developers.openai.com/api/docs/guides/image-generation) · [Prompting](https://developers.openai.com/api/docs/guides/image-prompting).

In some product tools the backend model is not exposed. Record the tool used and leave the exact model unknown. Do not infer model provenance from image quality or the wording of a prompt.

## The visual-director brief

```text
Asset and use: [README hero, slide, product photo, illustration]
Audience and message: [who it is for and what it should convey]
Subject: [concrete scene and required objects]
Composition: [framing, aspect ratio, useful negative space]
Style: [medium, lighting, palette and materials]
Exact copy: [only if words must appear]
Invariants: [identity, geometry, brand details or elements to preserve]
Avoid: [known unwanted elements]
Acceptance: [visual checks and required output files]
```

Create a small set of distinct directions, choose one, then refine specific issues. Use consistent palette, materials and composition across a package. Inspect text at its actual display size and review important details against references.

For diagrams with exact labels or quantitative charts, use deterministic drawing or plotting tools. This guide uses generated illustrations for atmosphere and Mermaid for the exact workflow relationship.

## This repository's artwork

The owner requested GPT Image 2.5, then explicitly accepted built-in generation without verified model identity because the available tool had no model selector. The assets were generated through that tool and inspected before publication. The [manifest](../assets/image-manifest.json) records the method, filenames and hashes; it makes no GPT Image 2.5 provenance claim.
