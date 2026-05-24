# Local Workspace Policy

Use this reference when a user wants local study notes, local environment files, virtual environments, datasets, logs, or scratch work near one or more repositories without committing them.

## Default layout

For a workspace that contains multiple repositories, prefer a sibling `_local/` directory:

```text
<workspace>/
+-- <repo-a>/
+-- <repo-b>/
+-- _local/
    +-- notes/
    |   +-- <repo-a>/
    |   +-- <repo-b>/
    |   +-- shared/
    +-- env/
    |   +-- <repo-a>/
    |   +-- <repo-b>/
    +-- venvs/
    |   +-- <repo-a>/
    |   +-- <repo-b>/
    +-- data/
    |   +-- samples/
    |   +-- outputs/
    +-- logs/
    +-- scratch/
```

If the user provides a local workspace path, use that. Otherwise infer the workspace parent from the repository root. For example, when the repository root is `<workspace>/<repo>`, the default local root is `<workspace>/_local`.

An environment variable may override the default:

```text
REPO_HANDOFF_LOCAL_ROOT=/path/to/_local
```

## What each directory is for

- `_local/notes/<repo>/`: personal study notes, source-reading logs, questions, diagrams, and task notes.
- `_local/notes/shared/`: cross-repository notes.
- `_local/env/<repo>/`: local environment files, secret-bearing configs, and deployment-local settings.
- `_local/venvs/<repo>/`: Python virtual environments or pointers to local runtimes.
- `_local/data/`: local samples and generated outputs that are not source truth.
- `_local/logs/`: runtime logs.
- `_local/scratch/`: temporary experiments and one-off scripts.

## Safety rules

- Do not commit `_local/` to any repository.
- Do not write `_local/` contents into `docs/ai_handoff/` by default.
- `_local/notes/<repo>/` may be read during `task-load` only when useful for the task or explicitly requested.
- Always label `_local/notes` evidence as `local/private`.
- Local notes never outrank current source code, `AGENTS.md`, or committed handoff docs.
- Never read, quote, summarize, or copy raw secret values from `_local/env/`.
- For env work, prefer committed safe examples such as `.env.example`, `.env.template`, or documented variable names.
- If the user explicitly asks about `_local/env/`, report filenames and required variable names where possible, not values.
- Do not use `_local/venvs/`, `_local/data/`, `_local/logs/`, or `_local/scratch/` as project truth unless the user explicitly asks.

## Local git excludes

For personal-only ignore rules, prefer each repository's `.git/info/exclude` instead of committing `.gitignore` changes. Useful local patterns:

```gitignore
.env
.env.*
!.env.example
.venv/
venv/
_local/
local/
notes/
study-notes/
scratch/
*.local.md
*.log
```

Only edit a repository's committed `.gitignore` when the user wants the rule shared with collaborators.

## Handoff usage

`llm_handoff.md` can mention that local notes exist and point to `_local/notes/<repo>/`, but it should not inline private notes. Snapshots may cite local notes only when the user requested that private context and the citation is clearly marked `local/private`.
