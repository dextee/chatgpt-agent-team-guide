# Set up your ChatGPT / Codex agent team

[Home](README.md) · [Product differences](docs/product-surfaces.md)

This setup installs **nine local Codex custom agents**. It does not configure ordinary ChatGPT Chat or hosted Work on the web. The definitions use the current [custom-agent TOML format](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## 1. Check prerequisites

- Current Codex CLI, desktop or IDE client with custom-agent support.
- Access to the selected models in your account/workspace.
- Python 3.11+ for this repository's installer.

```bash
codex --version
python --version
git clone https://github.com/dextee/chatgpt-agent-team-guide.git
cd chatgpt-agent-team-guide
```

On Windows, `py -3.12` can replace `python`. Review `scripts/install_agents.py` before running it.

## 2. Preview, then install

For one project:

```bash
python scripts/install_agents.py --project /path/to/project --dry-run
python scripts/install_agents.py --project /path/to/project
```

Windows example:

```powershell
py -3.12 scripts/install_agents.py --project 'C:\Projects\MyApp' --dry-run
py -3.12 scripts/install_agents.py --project 'C:\Projects\MyApp'
```

For personal agents, available across projects:

```bash
python scripts/install_agents.py --user --dry-run
python scripts/install_agents.py --user
```

Personal installs use `$CODEX_HOME/agents` when that environment variable is set, otherwise `~/.codex/agents`. Project installs use `<project>/.codex/agents`. Do not install a second copy into both scopes unless you intend to manage precedence yourself.

The installer validates all templates before writing, skips identical files, and backs up changed files under `.codex/agent-team-backups/<timestamp>/`. It refuses symlink, junction and hard-linked destinations. It stages each replacement before swapping the file into place. It does not edit `config.toml`, `AGENTS.md`, login state or permissions. Review its printed destination before proceeding.

## 3. Start a new Codex session

Open or trust the intended project using your normal client workflow. Start with:

```bash
codex -m gpt-6-sol -c model_reasoning_effort=medium
```

Ask:

```text
Use guide_explorer to identify this project's entry points and test commands.
Return only evidence with file references. Make no edits.
```

Confirm the client shows the expected custom agent and model. In CLI, `/agent` lets you inspect agent threads. Installation alone is not proof that your account can execute a model. If discovery fails, check scope, project trust, client version, TOML validity and the actual supported configuration before changing models.

## 4. Optional team defaults

The example in [config/codex.example.toml](config/codex.example.toml) is for review and manual merging. Copying it over your whole configuration would discard unrelated settings, so the installer intentionally does not do that.

The concurrency value is a local configuration cap, not an entitlement or a guarantee of available slots. Use fewer agents if they compete for the same files or session.

## Model-selection precedence

Current documentation says a custom agent file's `model` and `model_reasoning_effort` take precedence. Before that file is applied, explicit spawn settings, `[agents]` defaults and parent settings participate in resolution. Our templates set both values so a model does not accidentally inherit an unsuitable effort. [Official reference](https://learn.chatgpt.com/docs/agent-configuration/subagents).

To change a role, edit its two model fields deliberately and restart/reload as required by your client. Prompting a fixed-model role to use another model is not a reliable override.

Sandbox settings are subject to parent runtime policy and overrides. A `read-only` entry is a requested setting, not an independent guarantee against every external tool side effect. Verify effective permissions and tool access in the running session.

## Rollback

If an existing file was replaced, the installer prints its backup location. Restore that specific backup to the corresponding `agents/guide_*.toml` path. For newly added roles you no longer want, remove only their named files after confirming you have not customized them. No main settings or account state need rollback.

## What was tested here

The templates and installer have local static and filesystem checks. Live model execution is account-dependent and is not included in those checks. See [validation evidence](VALIDATION.md) for the exact completed gates.
