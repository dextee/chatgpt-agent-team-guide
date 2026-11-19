# Install the nine local Codex agents

[Home](README.md) · [Which product are you using?](docs/product-surfaces.md)

The installer adds nine named roles to your local Codex app, CLI or IDE setup. ChatGPT Work on the web can delegate hosted tasks directly when your account has access. In regular Chat, use the guide's briefs and review prompts. [Subagents by client](https://learn.chatgpt.com/docs/agent-configuration/subagents)

Checked **2026-11-20**. This edition uses GPT-6.2 Sol for the lead and four specialists, GPT-6.2 Astra for the architect and auditor, GPT-6.1 Terra for the visual director, and GPT-6 Luna for the explorer and mechanical worker. The lead is the parent session. The other nine roles are the files installed below. [Models and migration](docs/models-and-effort.md)

## 1. Check prerequisites

Use Python 3.11 or newer. For the supplied GPT-6.2 profiles, use Codex CLI **0.166.0 or later** or the Codex app with model access. Check the picker in the app or run `/model` in the CLI. [OpenAI client requirements](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)

The IDE extension reads local configuration too. OpenAI lists GPT-6.2 Sol and Astra for the app and CLI. If you also use the IDE, check its picker and choose a model available in each client for any shared role. OpenAI gives `gpt-6.1-sol` as one example. [Models by client](https://learn.chatgpt.com/docs/models)

```bash
codex --version
python --version
git clone https://github.com/dextee/chatgpt-agent-team-guide.git
cd chatgpt-agent-team-guide
```

On Windows, `py -3.12` can replace `python` if Python 3.12 is installed. The installer is available for inspection in [scripts/install_agents.py](scripts/install_agents.py).

## 2. Preview, then install

From the guide checkout, choose a scope. For one project, substitute its existing directory in both commands.

```bash
python scripts/install_agents.py --project /path/to/project --dry-run
python scripts/install_agents.py --project /path/to/project
```

These PowerShell commands install the roles into an existing project at `C:\Projects\MyApp`.

```powershell
py -3.12 scripts/install_agents.py --project 'C:\Projects\MyApp' --dry-run
py -3.12 scripts/install_agents.py --project 'C:\Projects\MyApp'
```

To make the roles available across local projects instead, install in the personal scope.

```bash
python scripts/install_agents.py --user --dry-run
python scripts/install_agents.py --user
```

| Scope | Destination | Backups for changed files |
|---|---|---|
| One project | `<project>/.codex/agents/` | `<project>/.codex/agent-team-backups/<timestamp>/` |
| Personal | `<CODEX_HOME>/agents/` | `<CODEX_HOME>/agent-team-backups/<timestamp>/` |

`CODEX_HOME` defaults to `~/.codex`. The personal installer honors a custom value set in its environment. Use the same personal Codex home in the client that will run these roles. [Codex home and trusted project configuration](https://learn.chatgpt.com/docs/config-file/config-advanced)

The preview lists files to add, replace or skip. Review the destination and any customized file marked for replacement. The installer validates the templates, skips identical files, checks linked destinations and verifies each staged replacement. Keep the printed backup path if you upgrade an existing installation.

## 3. Verify discovery in your project

Open the **destination project** in Codex. For a project-scoped installation, use a project you trust and follow your client's trust prompt. Codex skips project configuration layers when the workspace is untrusted. [Configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic)

In a terminal, change to that project before starting a fresh Codex session.

```bash
cd /path/to/project
codex -m gpt-6.2-sol -c model_reasoning_effort=medium
```

For the Windows example, use `Set-Location -LiteralPath 'C:\Projects\MyApp'` before the same `codex` command. If a read-only review is required, select **read-only** for the parent session before delegation. Try one named role first.

```text
Spawn one subagent using guide_explorer. Ask it to identify the project's
entry points and test commands without editing any files. Wait for it to
finish. Return the file references it checked and any commands it found.
```

Inspect the child thread through the app's activity or `/subagents` in the CLI. Confirm that the request produced a separate thread and that its references exist. If the client reports an unknown role or model, check the printed destination, project trust, client version and model picker. A successful file copy verifies installation only. [OpenAI subagent controls](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## 4. Optional team defaults

Review [config/codex.example.toml](config/codex.example.toml) and merge only the settings you want into your configuration. The example limits concurrently open child threads to three, excluding the primary session. Choose a lower cap when jobs compete for the same files. [OpenAI subagent settings](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## Model-selection precedence

These profiles set both `model` and `model_reasoning_effort`. A value in a custom role file takes precedence over the value resolved from the spawn request, then the corresponding `[agents]` default, then the parent. To change a role, edit its two fields, start a fresh session and run a familiar acceptance check. [Custom agent configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents)

**Permissions come from the parent session.** A role can request an inspection without edits in its instructions. For an enforced filesystem restriction, run that review under a read-only parent. A custom role cannot set its own sandbox, approval policy, provider or MCP servers. Review tools that can make external changes under their own permissions. [Subagent permissions](https://learn.chatgpt.com/docs/agent-configuration/subagents#approvals-and-sandbox-controls)

## Rollback

For a replaced role, restore its saved file from the printed backup directory to the corresponding `agents/guide_*.toml` path. For an added role, remove only that role's file after checking for local customizations. Revert any optional config entries you merged separately and start a fresh session.

## Validation evidence

The repository records installer and template checks separately from model execution. See the evidence for which checks ran, on which platform, and with what limits. [Validation record](VALIDATION.md)
