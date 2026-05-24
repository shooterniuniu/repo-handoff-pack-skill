# Repo Handoff Pack Skill

Reusable Codex skill for creating, loading, validating, and refreshing local
repository handoff memory under sibling `_local/handoff/<repo>/` workspaces.

The LLM-facing handoff is designed as a lightweight context index. Detailed
evidence stays in snapshots and is loaded on demand.

This repository is intended to be used as a standalone skill package. When
vendored into a project, the recommended project-local path is:

```text
.agents/skills/repo-handoff-pack/
```

## Commit

- `SKILL.md`
- `references/*.md`
- `assets/*.md`
- `assets/*.html`
- `agents/openai.yaml`
- `scripts/*.py`
- this `README.md`
- `.gitignore`

These files define the reusable workflow, templates, and optional helper
scripts. They should stay path-neutral and must not contain credentials,
machine-local state, or project-specific secrets.

## Do Not Commit

- `~/.codex/`, `~/.agents/`, or other whole agent home directories
- `auth.json`, session databases, logs, caches, browser state, or plugin caches
- `.env`, `.env.*` except intentional examples such as `.env.example`
- `_local/` workspace contents, including generated handoff artifacts, local
  notes, env files, venvs, data, logs, and scratch files
- generated runtime data, local recordings, or sandbox run outputs

## Cross-Device Use

Personal install from this repository root:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills\repo-handoff-pack" | Out-Null
Copy-Item -Recurse -Force ".\*" "$HOME\.agents\skills\repo-handoff-pack\"
```

On macOS or Linux:

```bash
mkdir -p "$HOME/.agents/skills/repo-handoff-pack"
cp -R ./* "$HOME/.agents/skills/repo-handoff-pack/"
```

Project-local vendored use from a project repository:

```powershell
New-Item -ItemType Directory -Force ".agents\skills\repo-handoff-pack" | Out-Null
Copy-Item -Recurse -Force "<path-to-this-repo>\*" ".agents\skills\repo-handoff-pack\"
```

On macOS or Linux:

```bash
mkdir -p ".agents/skills/repo-handoff-pack"
cp -R "<path-to-this-repo>/"* ".agents/skills/repo-handoff-pack/"
```

For team reuse across many repositories, vendor this repository by subtree,
submodule, or a release copy.

## Repository Policy

Generated handoff artifacts belong under sibling `_local/handoff/<repo>/` by
default:

```text
_local/handoff/<repo>/
+-- docs/
+-- snapshots/
+-- changes/
+-- state/
```

Use repository paths such as `docs/ai_handoff/` only when a user explicitly
wants committed/shared handoff docs, or when reading existing legacy handoff
docs during intake.

Reusable workflow files belong in this repository root, or under
`.agents/skills/repo-handoff-pack/` when vendored into another project.

Business code directories should not receive generated handoff documentation.

Personal study notes, source-reading logs, questions, diagrams, and other local
learning materials should live in sibling `_local/notes/<repo>/` by default.
Local environments should stay in `_local/env/<repo>/` when possible. Do not
copy secrets or raw local environment values into handoff artifacts.
