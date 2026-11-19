# Source register

[Home](README.md)

**Product facts checked on 2026-11-20.** The sources below support the product, configuration and API claims. The nine roles, their effort settings and the routes for the 24 tasks are this guide's recommendations. Evaluate those choices against the acceptance checks for your own work.

## Models, access and cost

| Source | What to verify |
|---|---|
| [GPT-6.2 release](https://learn.chatgpt.com/docs/whats-new/gpt-62-astra-sol) | November 17 release of GPT-6.2 Astra and Sol, supported surfaces, model selection and Work effort defaults |
| [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) | Differences between regular Chat and the Work and Codex selectors, and the effect of plan, seat and workspace settings |
| [Model selection](https://learn.chatgpt.com/docs/model-selection) | Suggested workloads for Astra, Sol, Terra and Luna, with advice on comparing settings |
| [Work and Codex models](https://learn.chatgpt.com/docs/models) | Product reasoning controls, context defaults and the difference between Max and Ultra |
| [API model catalog](https://developers.openai.com/api/docs/models) | Published API model IDs and reasoning levels for all four routes |
| [GPT-6.2 Astra](https://developers.openai.com/api/docs/models/gpt-6.2-astra) | Astra's API context, text-token rates, cache charges and long-context threshold |
| [GPT-6.2 Sol](https://developers.openai.com/api/docs/models/gpt-6.2-sol) | Sol's API context, text-token rates, cache charges and long-context threshold |
| [GPT-6.1 Terra](https://developers.openai.com/api/docs/models/gpt-6.1-terra) | Visual reasoning and computer use, API reasoning levels, tool support and prices |
| [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) | Focused high-volume work, API prices and the Chat Completions function-calling condition |
| [Using GPT-6.2](https://developers.openai.com/api/docs/guides/latest-model) | Responses API tool support for GPT-6.2 and migration guidance |
| [API reasoning guide](https://developers.openai.com/api/docs/guides/reasoning) | Model-dependent reasoning settings and rejection of `none` by both GPT-6.2 models |

## Delegation and installation

| Source | What to verify |
|---|---|
| [Subagents by client](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Hosted Work delegation, local TOML discovery and precedence, `/subagents`, concurrency and inheritance of parent permissions |
| [Configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic) | Trusted project `.codex/` layers and precedence of configuration files |
| [Advanced configuration](https://learn.chatgpt.com/docs/config-file/config-advanced) | `CODEX_HOME`, its default location and project-local configuration |
| [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference) | Parent configuration keys for agents, models and effort |
| [Responses multi-agent beta](https://developers.openai.com/api/docs/guides/responses-multi-agent) | Supported models, beta opt-in and sharing of the request's model and tools |
| [Agents SDK models and providers](https://developers.openai.com/api/docs/guides/agents/models) | Assigning different models to agents in an application |

## Images and project history

| Source | What to verify |
|---|---|
| [Image prompting](https://developers.openai.com/api/docs/guides/image-prompting) | GPT-Image-2.6 Flare for speed and Sunburst for detailed generation or precise edits |
| [Images API reference](https://developers.openai.com/api/reference/resources/images/methods/generate) | Model identifiers and explicit model selection when creating an image |
| [Image generation](https://developers.openai.com/api/docs/guides/image-generation) | Image generation workflows using Images and Responses |
| [Original Claude workflow at a fixed commit](https://github.com/dextee/vyr-agent-os-workflows/tree/d227750cba963e48eb38035d84c5d339c2d7f877) | The author's historical five-role structure and setup pattern |
| [Claude Code Agent Team Guide](https://github.com/dextee/claude-agent-team-guide) | Companion edition for Claude Code |

## Reading the evidence

- **Prices** are dated API list rates. Measure actual usage, tool charges and rework to calculate cost per accepted result. Subscription allowances have separate rules.
- **Role files** describe the intended routing. The client and workspace determine model availability. Session activity provides evidence of execution.
- **Validation** records the checks run against the guide, profiles and installer. Model quality needs an evaluation on representative inputs. [Validation record](VALIDATION.md)
- **Illustrations** explain concepts. The asset register records the available generation details. An exact backend can be attributed only when the tool or API identifies it. [Artwork provenance](assets/README.md)

## Keeping the guide current

When model guidance or agent behavior changes, check the affected source pages and revise the setup, model table, routing data, examples and verification date together. Keep older observations dated so readers can distinguish historical records from current instructions.

## 11 October 2026 refresh

The refresh rechecked GPT-6.1 Sol, Astra and Luna model pages, model selection, Work/Codex model controls, standalone custom-agent schema and precedence, native Responses multi-agent beta, and image-generation/prompting guidance. It updates the Sol default and cached-read rate, removes an unsupported derived input-token cap, and keeps product controls separate from API effort values. Historical review and image-generation records retain their original dates.
