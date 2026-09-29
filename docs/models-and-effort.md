# Models, reasoning and practical defaults

[Home](../README.md) · [Task selector](task-selector.md) · [Cost worksheet](cost-and-evaluation.md)

![Three model roles illustrated as complementary instruments](../assets/images/model-trio.png)

## Choose capability, then tune effort

Our usual lead is **Sol / medium**. Assign Luna a bounded task whose output you can check cheaply. Use Astra for difficult decisions, broad synthesis or demanding final review. These choices are guide recommendations; measure performance on your own work.

| API model ID | Standard input / cached read / output, USD per 1M tokens | API reasoning levels |
|---|---|---|
| [`gpt-6-luna`](https://developers.openai.com/api/docs/models/gpt-6-luna) | $0.10 / $0.01 / $0.50 | none, low, medium, high, xhigh, max |
| [`gpt-6-sol`](https://developers.openai.com/api/docs/models/gpt-6-sol) | $2.00 / $0.20 / $10.00 | none, low, medium, high, xhigh, max |
| [`gpt-6-astra`](https://developers.openai.com/api/docs/models/gpt-6-astra) | $10.00 / $1.00 / $50.00 | low, medium, high, xhigh, max |

The model pages currently list a 1,050,000-token context window, up to 922,000 input tokens and 128,000 output tokens for these models. Do not assume every app exposes the API maximum. For prompts above 272K input tokens, the listed full-request rates increase: input/cache at 2x and output at 1.5x. Other modes and tools can change the total. See the linked model pages before budgeting.

## Our effort ladder

| Start | Work shape | Increase effort when |
|---|---|---|
| Low | One clear transformation | A useful constraint is repeatedly missed |
| Medium | Everyday execution | Several dependencies or edge cases need analysis |
| High | Investigation or review | The task still needs substantially deeper reasoning |
| Extra high / max | Exceptional reasoning depth | A comparison shows better completed results |

The installed agents deliberately vary their settings. Luna's explorer uses high to trace references; its mechanical worker uses medium. Astra's architect uses high because that role is reserved for harder decisions. These are task-specific settings rather than a claim about each model's default.

**Ultra is product orchestration behavior.** Work/Codex documentation describes it as maximum reasoning with delegation. Luna supports Max, but not Ultra. The API model pages above do not list `ultra` as a `reasoning.effort` value. Do not paste it into an API request. [Product model controls](https://learn.chatgpt.com/docs/models).

## Set the model in the right place

Local Codex launch:

```bash
codex -m gpt-6-sol -c model_reasoning_effort=medium
```

Local custom agent: edit the `model` and `model_reasoning_effort` keys in its TOML file. In the ChatGPT Work interface, use the model and intelligence control. Check actual availability instead of inferring entitlement from an identifier. [Setup](../SETUP.md).

API consumers should prefer Responses for these agent workflows. Sol and Luna have additional function-calling restrictions in Chat Completions; see their model pages. The guide's installable files are **Codex configuration**, not API request bodies.

## A useful escalation packet

Send the stronger model the objective, relevant evidence, attempted approaches, observed failure and the decision you need. Return the resolved decision to the original worker when practical. This avoids resending every exploratory log while preserving what matters.
