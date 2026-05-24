# Output Contract

Use this reference when creating or refreshing handoff artifacts.

## Directories

- Project memory: `docs/ai_handoff/`
- Snapshots: `docs/ai_handoff/snapshots/`
- Incremental refresh reports: `docs/ai_handoff/changes/`
- Skill resources: `.agents/skills/repo-handoff-pack/`
- Optional local/private workspace: sibling `_local/` directory, such as `<workspace>/_local/`

Generated handoff artifacts must stay under `docs/ai_handoff/`. Skill templates, references, and optional scripts stay under `.agents/skills/repo-handoff-pack/`.

Do not write `_local/` contents into generated handoff artifacts by default. When local notes are explicitly useful, cite them as `local/private` and keep secrets out of committed docs.

## Required artifacts by mode

| Mode | Required outputs |
| --- | --- |
| `bootstrap` | `AGENTS.md` handoff section, `docs/ai_handoff/HANDOFF_STATE.md`, `docs/ai_handoff/snapshots/` |
| `onboarding-intake` | `snapshots/00_onboarding_intake.md`, `HANDOFF_STATE.md`, maybe lightweight `llm_handoff.md` |
| `full-build` | Phase snapshots, `human_overview.html`, lightweight `llm_handoff.md`, `llm_handoff.html`, `HANDOFF_STATE.md` |
| `task-load` | No file changes; summary and task plan only |
| `post-change-refresh` | Affected snapshots, final docs, state, `changes/YYYY-MM-DD_post_change_refresh.md` |
| `drift-check` | No file changes; drift report only |

## Handoff state sections

`HANDOFF_STATE.md` must include:

- Handoff metadata
- Completed phases
- Last updated snapshots
- Last changed source files
- Known unknowns
- Detected conflicts
- Next recommended action
- Resume instruction
- Refresh policy

## HTML requirements

- Single file.
- Inline CSS only.
- No external network resources.
- Human-readable headings.
- Path-specific evidence and explicit unknowns.

## LLM handoff requirements

- Markdown.
- Concise, structured, and task-oriented.
- Act as a context index and routing map, not a full repository digest.
- Include key files, entrypoints, task routes, snapshot index, command map, constraints, do-not-touch areas, unknowns, conflicts, and next tasks.
- Link to detailed snapshots instead of inlining exhaustive architecture, chain/tool/schema/state/prompt/test details.
- Mention local/private notes only as optional paths to read on demand; never inline secrets or raw environment values.

## Human overview requirements

- Human-readable and more complete than the LLM index.
- May synthesize detailed architecture, workflows, risks, and operating guidance.
- Must still use path-specific evidence and explicit unknowns.
