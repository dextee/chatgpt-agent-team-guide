# Which product are you using?

[Home](../README.md) · [Local Codex setup](../SETUP.md)

You can use the briefs in ordinary **Chat**, delegate hosted work in **ChatGPT Work**, or install the nine named roles in **local Codex**. API developers can also build their own routing. The controls below were checked on **2026-11-20**.

| Surface | Where to start | How to check what ran |
|---|---|---|
| Regular Chat | Paste a brief and ask for a draft, review and revision. Use the models shown in the Chat picker. | Inspect the staged results in the conversation. To select GPT-6.2 Astra or Sol, open Work or Codex. |
| ChatGPT Work on the web | Choose a model in the composer. Ask for subagents explicitly at most intelligence levels. On eligible accounts, Ultra can delegate suitable work proactively. | Open **Subagents** for activity and completed results. The web list is read-only. |
| Local Codex app, CLI or IDE | Install the project's role files. Ask Codex to spawn a named role, or include delegation in applicable project or skill instructions. | Inspect the agent threads. In the CLI, use `/subagents`. |
| Responses API multi-agent beta | Enable native delegation for a request that uses a supported model. | Inspect the response events for actual spawns and results. Each child shares the request's model and available tools. |
| Application using the Agents SDK | Define an agent per role and set its model in application code when roles need different models. | Check the agent definitions and run traces. API billing applies to SDK requests made with your API credentials. |

Regular Chat has its own model picker. The Help Center describes GPT-6 Sol as powering the GPT-6 option in regular Chat. GPT-6.2 Astra and Sol are selected in Work or Codex, subject to plan, seat and workspace settings. For Work on the web, subagents run in the hosted environment with the tools available to the parent chat. [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) · [Subagents by surface](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## Try it in ChatGPT Work

```text
Prepare a sourced decision brief for [question]. Ask one subagent to find
supporting evidence, another to find counterevidence, and a third to
identify missing information. Wait for their findings.
Cite the original sources, reconcile conflicts and list unresolved questions.
If this chat has no subagent access, complete the three checks in sequence.
```

Naming a role describes the work you want. Use the activity panel to confirm a child actually ran and the client-provided model information to check its model when available. The local TOML installer applies only to local Codex clients. [Hosted and local subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## Try it in local Codex

After installation, open a trusted project and give the roles independent questions first. Writing to the same files is easier to coordinate when one person or agent owns the changes. [Setup](../SETUP.md)

```text
Spawn guide_explorer to locate the order-validation entry points and
guide_reviewer to identify missing tests from the specification. Ask both
to work without editing. Wait for both results. Give guide_implementer
the agreed changes, then report the tests actually run.
```

For an enforced read-only review, select read-only permissions for the **parent session** before delegation. Local children inherit its sandbox and approvals. A role's review instructions describe its job and cannot enforce a separate permission boundary. [Subagent permissions](https://learn.chatgpt.com/docs/agent-configuration/subagents#approvals-and-sandbox-controls)

## Choose API orchestration

Use the **Responses API multi-agent beta** when independent children can share the root request's model and tools. The documented list includes GPT-6.2 Astra, GPT-6.2 Sol, GPT-6.1 Sol and the GPT-5.6 models. Enable `multi_agent.enabled` and use the documented beta opt-in for your SDK or HTTP client. Inspect the resulting activity to see which tasks the model delegated. [Responses API multi-agent guide](https://developers.openai.com/api/docs/guides/responses-multi-agent)

Use the **Agents SDK** when each job requires an explicit model, for example Luna for intake and Astra for complex decisions. Configure each agent in application code and supply its tools there. This repository supplies prompts, routing data and local Codex profiles. Running an API service requires an application and API access. [SDK model configuration](https://developers.openai.com/api/docs/guides/agents/models)
