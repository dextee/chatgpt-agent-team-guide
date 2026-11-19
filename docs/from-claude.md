# What carries over from the Claude guide?

[Home](../README.md)

The reference is the author's [original Claude guide at commit d227750](https://github.com/dextee/vyr-agent-os-workflows/tree/d227750cba963e48eb38035d84c5d339c2d7f877). That repository was later renamed and repurposed; the commit preserves the guide that informed this structure. The current Claude edition now lives at [dextee/claude-agent-team-guide](https://github.com/dextee/claude-agent-team-guide).

The roles carry over as assignments. Choose the model separately in the product you use. This edition uses **GPT-6.2 Sol** (`gpt-6.2-sol`) for everyday implementation and **GPT-6.2 Astra** (`gpt-6.2-astra`) for complex design and review decisions. [Model choices and client access](models-and-effort.md)

| Original idea | This guide's implementation |
|---|---|
| Architect resolves hard decisions | `guide_architect`, Astra / high |
| Implementer completes the build | `guide_implementer`, Sol / medium |
| Worker owns a bounded chunk | `guide_worker`, Luna / medium for mechanical work; use the implementer for judgment-heavy chunks |
| Explorer gathers evidence | `guide_explorer`, Luna / high |
| Independent auditor checks the result | `guide_auditor`, Astra / high for complex decisions, or a Sol reviewer for routine changes |
| Reusable setup and workflow prompts | Portable installer, TOML files and scenario recipes |
| A strong advisor helps at decision points | Delegate a bounded consultation to the architect; this is a workflow pattern |

For an architectural consultation, ask Codex to spawn `guide_architect` with the decision, constraints and expected return. For screenshots or visual evidence, this edition also includes `guide_visual_director`, configured for GPT-6.1 Terra at medium effort. Install the Codex TOML files and choose an available model for each role. [Codex setup](../SETUP.md)

The original model assignments are historical. This guide makes no claim that Claude models and GPT models are equivalent or that one vendor wins a workload. Its current OpenAI facts come from the [source register](../SOURCES.md).
