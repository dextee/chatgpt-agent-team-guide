# Make useful, coherent images

[Home](../README.md) · [Artwork gallery](../assets/README.md)

![A visual brief moves through exploration, refinement and inspection](../assets/images/guide-image-workflow.png)

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

## A production prompt you can adapt

```text
Create a landscape editorial teaching illustration for a coordinated AI team.
Show a lead worktable receiving evidence from three separate stations:
a magnifying lens over source pages, hands making a paper prototype,
and a reviewer comparing the result with a checklist.
Keep each job distinct and the scene legible at small display sizes.

Art direction: tactile cut paper, navy pen contours and restrained shadows.
Warm ivory #F7F3EA, navy #172F40, teal #147B77, coral #E56F52,
muted ochre #DDB76F. Matte paper, painted wood and calm daylight.
Composition: wide framing and generous margins. No generated words,
logos, fake product screens or performance claims.
Preserve the same materials, palette and worktable identities in variants.
Deliver a clean opaque image; inspect object edges and the intended crop.
```

After choosing a direction, name the precise edit: “Move the making station right to open the title area; preserve the other worktables, palette, lighting and camera angle.” Compare the original and revision at the intended display size. Add accurate labels in the document layout when exact text matters. The [October prompt collection](../assets/new-prompts.json) records the exact instructions used for this guide.

## Explicit API selection

Examples checked against the [official generation guide](https://developers.openai.com/api/docs/guides/image-generation) on **2026-10-11**. They require a current OpenAI Python SDK, API access and an `OPENAI_API_KEY` environment variable; executing them makes a billed API request. These are documented examples, not claims that this repository's artwork used those models.

For a single asset, choose the image model directly:

```python
import base64
from pathlib import Path
from openai import OpenAI

client = OpenAI()
output = Path("team-concept-sunburst.png")
if output.exists():
    raise FileExistsError(output)
result = client.images.generate(
    model="gpt-image-2.5-sunburst",
    prompt="An editorial ivory-and-glass diorama of a lead worktable and three "
           "specialist stations in mint, amber and violet. Midnight navy backdrop. "
           "Wide composition, empty title area on the left. No text or logos.",
    size="1536x1024",
    quality="high",
    background="opaque",
    output_format="png",
)
with output.open("xb") as file:
    file.write(base64.b64decode(result.data[0].b64_json))
```

For a speed-focused comparison, change the exact model to `gpt-image-2.5-flare` and use a new filename. Keep the prompt, dimensions and quality setting fixed for the initial comparison. Inspect the output; an identical quality label does not promise identical quality or latency. [Prompting guidance](https://developers.openai.com/api/docs/guides/image-prompting).

For a conversational workflow, the text model and image tool have separate IDs:

```python
import base64
from pathlib import Path
from openai import OpenAI

client = OpenAI()
output = Path("team-concept-response.png")
if output.exists():
    raise FileExistsError(output)
response = client.responses.create(
    model="gpt-6.1-sol",
    reasoning={"effort": "medium"},
    input="Generate an ivory-and-glass editorial diorama of a central lead "
          "and three distinct specialist workstations. No text or logos.",
    tools=[{"type": "image_generation", "model": "gpt-image-2.5-sunburst"}],
)
images = [item.result for item in response.output
          if item.type == "image_generation_call"]
if not images:
    raise RuntimeError("The response did not return a generated image")
with output.open("xb") as file:
    file.write(base64.b64decode(images[0]))
```

GPT-6.1 Sol supports the Responses image-generation tool. [Supported tools](https://developers.openai.com/api/docs/models/gpt-6.1-sol). Use the Image API for a straightforward one-image job and Responses when conversation and iterative editing are useful.

## This repository's artwork

The repository's built-in generation tool did not expose its exact backend. The [manifest](../assets/image-manifest.json) records generation method, filenames, dimensions, inspection records and hashes. Original artwork retains its original generation date; refreshed artwork needs its own record. A requested model name and an accepted image do not establish exact GPT Image 2.5 provenance.
