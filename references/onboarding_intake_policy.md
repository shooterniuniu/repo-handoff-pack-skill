# Onboarding Intake Policy

Use for `onboarding-intake` when joining an unfamiliar repository or inheriting someone else's handoff docs.

## Read order

1. `AGENTS.md` and other agent instruction files.
2. `docs/ai_handoff/HANDOFF_STATE.md`.
3. Existing `docs/ai_handoff/llm_handoff.md`.
4. Existing `docs/ai_handoff/snapshots/*.md`.
5. README, architecture docs, runbooks, ADRs, operations docs, and imported handoffs.
6. A small set of source files only for critical claim validation.

Read only snapshots that are relevant to the intake goal. Use `llm_handoff.md` as an index when it is present.

## Critical-claim validation

Validate claims that affect immediate work:

- entrypoints and run/test commands
- framework or package boundaries
- agent/workflow/tool behavior
- schemas, state, persistence, prompts, and safety constraints
- do-not-touch areas and generated directories

Use path-specific evidence. Do not validate every statement.

## Output

Write `docs/ai_handoff/snapshots/00_onboarding_intake.md` with:

- documents read
- inherited project summary
- critical claims reviewed
- validated claims
- unvalidated inherited context
- conflicts using the standard conflict format
- task-load guidance
- unknowns and next recommended action

Update `HANDOFF_STATE.md`. Create or refresh `llm_handoff.md` only if missing or stale enough that `task-load` would mislead a future agent. When refreshing it, keep it as a lightweight context index and route detailed inherited context to snapshots.

## Staleness signals

- Docs reference files or directories that no longer exist.
- Docs omit major current entrypoints, packages, or workflows.
- `HANDOFF_STATE.md` last changed files do not include recent source changes.
- Current `AGENTS.md` conflicts with handoff docs.

## Rules

- Preserve useful inherited context with a confidence label.
- Do not rewrite all repository documentation blindly.
- Do not run broad source scans.
- Mark uncertainty rather than filling gaps from inference.
