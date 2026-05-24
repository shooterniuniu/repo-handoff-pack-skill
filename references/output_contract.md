# Output Contract

Use this reference when creating or refreshing handoff artifacts.

## Directories

- Project memory: `docs/ai_handoff/`
- Snapshots: `docs/ai_handoff/snapshots/`
- Incremental refresh reports: `docs/ai_handoff/changes/`
- Skill resources: `.agents/skills/repo-handoff-pack/`

Generated handoff artifacts must stay under `docs/ai_handoff/`. Skill templates, references, and optional scripts stay under `.agents/skills/repo-handoff-pack/`.

## Required artifacts by mode

| Mode | Required outputs |
| --- | --- |
| `bootstrap` | `AGENTS.md` handoff section, `docs/ai_handoff/HANDOFF_STATE.md`, `docs/ai_handoff/snapshots/` |
| `onboarding-intake` | `snapshots/00_onboarding_intake.md`, `HANDOFF_STATE.md`, maybe `llm_handoff.md` |
| `full-build` | Phase snapshots, `human_overview.html`, `llm_handoff.md`, `llm_handoff.html`, `HANDOFF_STATE.md` |
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
- Include key files, entrypoints, architecture, chain/tool/schema/state/prompt/test summaries, constraints, do-not-touch areas, unknowns, conflicts, and next tasks.
