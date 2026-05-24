# Progressive Disclosure Policy

Use this reference when creating, refreshing, or loading LLM-facing handoff artifacts.

## Goal

`docs/ai_handoff/llm_handoff.md` is a context index, not a full repository digest. It should help a future LLM decide what to read next without spending context on every detail up front.

Humans can use `docs/ai_handoff/human_overview.html` and detailed snapshots for broader reading. LLM agents should start with the index, then load only task-relevant snapshots, local notes, and source files.

## Default read order for task-load

1. `AGENTS.md`
2. `docs/ai_handoff/HANDOFF_STATE.md`
3. `docs/ai_handoff/llm_handoff.md`
4. Snapshot files referenced by the task route
5. Task-relevant source files
6. Task-relevant `_local/notes/<repo>/` files only when useful or requested

Do not read every snapshot by default. Do not read local environment files for values.

## LLM handoff shape

`llm_handoff.md` should stay concise and include:

- handoff metadata
- how to resume
- project purpose in a few bullets
- task routing table: task type, files to read, snapshots to read, commands to consider
- snapshot index: path, topic, when to read, freshness/confidence
- key source map: path, role, why it matters
- command map with verification status
- source-of-truth and conflict notes
- constraints, do-not-touch areas, unknowns, and next actions

Avoid long architecture prose, copied code, full tool inventories, exhaustive schemas, and lengthy historical notes in `llm_handoff.md`. Put those details in snapshots and link them from the index.

## Snapshot shape

Snapshots are the detailed fact store. Each snapshot should include:

- scope and reason to read this snapshot
- files read and evidence paths
- facts, confidence, conflicts, and unknowns
- recommended next reads
- refresh triggers

Prefer several focused snapshots over one large undifferentiated handoff file.

## Final synthesis

During `full-build` Phase 5 or `post-change-refresh`:

- Generate `human_overview.html` for complete human-readable overview.
- Generate `llm_handoff.md` as a lightweight index and routing map.
- Regenerate `llm_handoff.html` from the lightweight index, not from all snapshot content.
- Preserve detailed evidence in `docs/ai_handoff/snapshots/*.md`.

Only reread source files when snapshots identify a specific critical gap.

## Drift and refresh

If a detailed snapshot changes, update the `llm_handoff.md` route or freshness row that points to it. If only prose inside a snapshot changes without changing task routing, keep the LLM index small and update its timestamp/confidence only when necessary.
