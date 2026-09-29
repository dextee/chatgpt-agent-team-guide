# Source register

[Home](README.md)

**Verification date: 2026-09-29.** Technical product statements use official OpenAI documentation. Scenario-to-model assignments, team composition and workflow prompts are the author's recommendations, inferred from those capabilities. They have not been benchmarked as a universal ranking.

| Source | Used to establish |
|---|---|
| [Model selection](https://developers.openai.com/api/docs/guides/model-selection) | General roles of Astra, Sol and Luna; selection as a workload tradeoff |
| [GPT-6 model guidance](https://developers.openai.com/api/docs/guides/latest-model) | Current family and API reasoning/tool distinctions |
| [GPT-6 Astra model](https://developers.openai.com/api/docs/models/gpt-6-astra) | Model ID, supported effort, API pricing and context details |
| [GPT-6 Sol model](https://developers.openai.com/api/docs/models/gpt-6-sol) | Model ID, supported effort, API pricing and context details |
| [GPT-6 Luna model](https://developers.openai.com/api/docs/models/gpt-6-luna) | Model ID, supported effort, API pricing and context details |
| [Work and Codex models](https://learn.chatgpt.com/docs/models) | Product availability, model controls and Ultra behavior |
| [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Local custom agents, required TOML fields, precedence and delegation |
| [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference) | Model, effort, sandbox and agent configuration keys |
| [Responses multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent) | Native API children share the request's model and tools |
| [Agents SDK models and providers](https://developers.openai.com/api/docs/guides/agents/models) | Application-owned per-agent model selection |
| [Image generation](https://developers.openai.com/api/docs/guides/image-generation) | GPT Image 2.5 identifiers and explicit API selection |
| [Image prompting](https://developers.openai.com/api/docs/guides/image-prompting) | Flare/Sunburst positioning and image brief guidance |
| [Original Claude guide, fixed commit](https://github.com/dextee/vyr-agent-os-workflows/tree/d227750cba963e48eb38035d84c5d339c2d7f877) | Author's historical five-role structure and setup pattern |

## Claim boundaries

- “Recommended” means this guide's proposed starting configuration, unless explicitly attributed to OpenAI.
- API list rates are date-specific and do not establish subscription allowance or actual completed-task cost.
- Model identifiers and configuration files do not prove account entitlement or live execution.
- Local parsing and installer tests do not constitute a model-quality evaluation.
- Generated illustrations are conceptual, not product screenshots or measured diagrams.
- The exact backend used for this repository's built-in image generation was not exposed. No exact model provenance is asserted.

## Keeping the guide current

Recheck model pages, product availability and custom-agent schema when upgrading. If a fact changes, update the affected files, routing data, examples and verification date together. Keep recommendations separate from the source facts that motivate them.
