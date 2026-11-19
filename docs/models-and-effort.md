# Models, reasoning and practical defaults

[Home](../README.md) · [Task selector](task-selector.md) · [Cost worksheet](cost-and-evaluation.md)

## Choose a model

For everyday work in this guide, start with **GPT-6.2 Sol at medium effort**. These are the author's starting choices. Try a familiar task, check the result and record how much editing it took. Model availability depends on your plan, client and workspace settings. Checked **2026-11-20**. [OpenAI model selection](https://learn.chatgpt.com/docs/model-selection)

| Model | When to try it | An acceptance check |
|---|---|---|
| GPT-6 Luna | A large set of short, repeatable tasks with explicit rules | Every output uses an allowed label and flags ambiguous inputs. |
| GPT-6.1 Terra | Work that depends on reading an image, chart or application screen | Compare the result with the source image or check the updated record in the app. |
| GPT-6.2 Sol | Everyday coding, writing, research and work across tools | Run the affected tests or trace the claims in the draft back to their sources. |
| GPT-6.2 Astra | A design decision, difficult diagnosis or synthesis across conflicting sources | Check whether the evidence rules out the strongest alternative explanation. |

Terra can inspect an image and describe an edit. The visual director uses a separate image-generation tool when the deliverable calls for new or edited artwork. [Image workflow](image-workflow.md)

## API prices and reasoning settings

Standard short-context text prices in USD per million tokens, checked **2026-11-20**. The linked model pages distinguish cache reads from writes. [OpenAI API model catalog and reasoning options](https://developers.openai.com/api/docs/models)

| API model ID | Standard input / cached read / output, USD per 1M tokens | API reasoning levels |
|---|---|---|
| [`gpt-6-luna`](https://developers.openai.com/api/docs/models/gpt-6-luna) | $0.10 / $0.01 / $0.50 | none, low, medium, high, xhigh, max |
| [`gpt-6.1-terra`](https://developers.openai.com/api/docs/models/gpt-6.1-terra) | $1.00 / $0.05 / $5.00 | none, low, medium, high, xhigh, max |
| [`gpt-6.2-sol`](https://developers.openai.com/api/docs/models/gpt-6.2-sol) | $2.00 / $0.10 / $10.00 | low, medium, high, xhigh, max |
| [`gpt-6.2-astra`](https://developers.openai.com/api/docs/models/gpt-6.2-astra) | $8.00 / $0.40 / $40.00 | low, medium, high, xhigh, max |

For all four models, a request over 272,000 input tokens costs twice the short-context input and cache rates and 1.5 times the output rate for the full request. The API model pages list 1,050,000 tokens of context and up to 128,000 output tokens. Local Codex has its own defaults, including 272,000 tokens of context for GPT-6.2 Astra and 500,000 for GPT-6.2 Sol. [Work and Codex models](https://learn.chatgpt.com/docs/models)

## Tune effort to the work

| Start | Work shape | Increase effort when |
|---|---|---|
| Low | One clear transformation | The result repeatedly misses a constraint. |
| Medium | Everyday execution | Several dependencies or edge cases need analysis. |
| High | Investigation or review | The model needs to test an alternative explanation. |
| Extra high or max | A difficult decision with evidence on both sides | Compare the result with a lower-effort run before adopting this setting. |

The templates use Luna at high effort for exploration and medium for mechanical work. The architect and auditor use Astra at high effort. These settings reflect the jobs assigned in this guide. OpenAI recommends starting GPT-6.2 Astra and Sol with the effort the client selects. Eligible new consumer Work chats default to Sol at Light, while Enterprise workspaces with model access default to Sol at Medium. [GPT-6.2 release](https://learn.chatgpt.com/docs/whats-new/gpt-62-astra-sol) · [Work and Codex effort controls](https://learn.chatgpt.com/docs/models)

In supported Work and Codex clients, **Max** gives one model more reasoning time. **Ultra** can divide work among subagents. Luna's product settings stop at Max. In an API request, choose one of the model's reasoning values in the table above. [Work and Codex models](https://learn.chatgpt.com/docs/models) · [API reasoning guide](https://developers.openai.com/api/docs/guides/reasoning)

## Set or change a model

This command starts a local Codex session with the guide's recommended lead and effort.

```bash
codex -m gpt-6.2-sol -c model_reasoning_effort=medium
```

In a custom agent file, set both `model` and `model_reasoning_effort` for that role. In ChatGPT Work, use the composer control and open **Advanced** if you see the Power slider. For an API application that needs tools with GPT-6.2 Astra, GPT-6.2 Sol or GPT-6.1 Terra, use Responses. Luna also permits Chat Completions function calling at `reasoning_effort=none`. [Codex setup](../SETUP.md) · [GPT-6.2 API guide](https://developers.openai.com/api/docs/guides/latest-model) · [Terra](https://developers.openai.com/api/docs/models/gpt-6.1-terra) · [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna)

When upgrading from the October edition, check the new models in your client, preview the installation and repeat a task whose expected result you know. The older roles used `gpt-6.1-sol` and `gpt-6-astra`. For a role you customized, compare your instructions and effort settings with the new file before replacing it. [Setup and rollback](../SETUP.md) · [October review](../PATCH_NOTES_20261011.md)
