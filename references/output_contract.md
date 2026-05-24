# Output Contract

Use this reference when creating or refreshing handoff artifacts.

## Directories

- Local handoff root: `_local/handoff/<repo>/`
- Final handoff docs: `_local/handoff/<repo>/docs/`
- Snapshots: `_local/handoff/<repo>/snapshots/`
- Incremental refresh reports: `_local/handoff/<repo>/changes/`
- Handoff state: `_local/handoff/<repo>/state/HANDOFF_STATE.md`
- Skill resources: `.agents/skills/repo-handoff-pack/`
- Personal/local learning materials: `_local/notes/<repo>/`
- Local environment materials: `_local/env/<repo>/`
- Optional local/private workspace: sibling `_local/` directory, such as `<workspace>/_local/`

Generated handoff artifacts must stay under `_local/handoff/<repo>/` by default. Personal study notes, source-reading logs, questions, diagrams, and local task notes are not handoff artifacts; write them under `_local/notes/<repo>/` by default. Skill templates, references, and optional scripts stay under `.agents/skills/repo-handoff-pack/`.

Use `docs/ai_handoff/` only when the user explicitly asks for committed/shared repository handoff docs or when reading existing legacy handoff files. Do not copy local notes or local environment contents into committed docs. When local notes are explicitly useful, cite them as `local/private` and keep secrets out of all artifacts.

## Required artifacts by mode

| Mode | Required outputs |
| --- | --- |
| `bootstrap` | `_local/handoff/<repo>/state/HANDOFF_STATE.md`, `_local/handoff/<repo>/snapshots/`, optional `AGENTS.md` only when explicitly requested |
| `onboarding-intake` | `snapshots/00_onboarding_intake.md`, `state/HANDOFF_STATE.md`, maybe lightweight `docs/llm_handoff.md` |
| `full-build` | Phase snapshots, `docs/human_overview.html`, lightweight `docs/llm_handoff.md`, `docs/llm_handoff.html`, `state/HANDOFF_STATE.md` |
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
