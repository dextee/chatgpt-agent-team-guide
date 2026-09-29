# Which product are you using?

[Home](../README.md) · [Setup](../SETUP.md)

| Surface | What this guide means there | What to check |
|---|---|---|
| ChatGPT Chat | Use the task briefs and staged review prompts with the models actually offered | Sol/Luna are documented for Work and Codex, not Chat |
| ChatGPT Work | Ask explicitly for independent subagents where available; choose the main model/intelligence level | Account eligibility and available tools; local TOML files are not a hosted-web installation method |
| Local Codex: desktop, CLI, IDE | Install the custom agent files for different role models | Current client, model entitlement, project trust and effective settings |
| Responses API native multi-agent beta | Enable the service's native delegation for independent work | Native children share the request's model and tools |
| Application-owned Agents SDK workflow | Define role agents and choose their models in your application | API credentials, orchestration, tools and separate API billing |

Sources: [product models](https://learn.chatgpt.com/docs/models), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Responses multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent), [SDK models and providers](https://developers.openai.com/api/docs/guides/agents/models).

## ChatGPT Work prompt

```text
Prepare a sourced decision brief for [question]. Use parallel subagents for
independent questions if this workspace supports them: one for evidence,
one for alternatives, and one for gaps. Wait for their findings, reconcile
conflicts, and return a recommendation with citations and open questions.
If delegation or model overrides are unavailable, say so and complete the
stages sequentially with the available model.
```

The named roles describe work. They do not prove that distinct models were used. Inspect the client-provided activity or configuration to confirm actual routing.

## Local Codex prompt

```text
Use guide_explorer to identify the affected files, then guide_architect to
resolve the design questions. Delegate only independent, bounded work.
Use guide_implementer for the implementation and guide_reviewer for review.
Return the final result and the checks actually performed.
```

Install those role definitions first. They are distinct from generic built-in agent names.

## API distinction that matters

`multi_agent.enabled` in the Responses API does not, by itself, create a mixed Astra/Sol/Luna team. Its native subagents share the root request's model. Use an application-owned agent workflow when distinct model choices per role are a requirement. The [Agents SDK model guide](https://developers.openai.com/api/docs/guides/agents/models) documents per-agent model selection.

This repository includes model-routing data and local Codex templates, not a deployed API service. No API key is needed to read the guide or install the TOML files; account access is required to run the selected models.
