# What carries over from the Claude guide?

[Home](../README.md)

The reference is the author's [original Claude guide at commit d227750](https://github.com/dextee/vyr-agent-os-workflows/tree/d227750cba963e48eb38035d84c5d339c2d7f877). The repository was subsequently renamed and repurposed; the commit preserves the guide that informed this structure.

| Original idea | This guide's implementation |
|---|---|
| Architect resolves hard decisions | `guide_architect`, Astra / high |
| Implementer completes the build | `guide_implementer`, Sol / medium |
| Worker owns a bounded chunk | `guide_worker`, Luna / medium for mechanical work; use the implementer for judgment-heavy chunks |
| Explorer gathers evidence | `guide_explorer`, Luna / high |
| Independent auditor checks the result | `guide_auditor`, Astra / high; Sol reviewer for routine changes |
| Reusable setup and workflow prompts | Portable installer, TOML files and scenario recipes |
| A strong advisor helps at decision points | Delegate a bounded consultation to the architect; this is a workflow pattern |

The last row does not imply a Claude-style `/advisor` command in Codex. Likewise, `.claude` plugin manifests, Claude model aliases and Claude effort defaults do not configure an OpenAI agent.

The original model assignments are historical. This guide makes no claim that Claude models and GPT models are equivalent or that one vendor wins a workload. Its current OpenAI facts come from the [source register](../SOURCES.md).
