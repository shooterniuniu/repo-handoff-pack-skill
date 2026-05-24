# Lifecycle Modes

Use this reference to choose and execute one handoff mode. Prefer the narrowest mode that answers the user request.

## Mode decision table

| Situation | Mode | File changes |
| --- | --- | --- |
| No `docs/ai_handoff/` or handoff guidance exists | `bootstrap` | Structure/state/workflow only |
| Inherited docs exist and repository is unfamiliar | `onboarding-intake` | Intake snapshot, state, maybe `llm_handoff.md` |
| No reliable handoff exists | `full-build` | Staged snapshots and final docs |
| Starting a normal coding task | `task-load` | None unless explicitly requested |
| Code changed and docs should be refreshed | `post-change-refresh` | Affected snapshots, final docs, state, change report |
| Need to know if docs are stale | `drift-check` | None unless explicitly requested |

## bootstrap

Create or update the handoff workflow section in `AGENTS.md`, create `docs/ai_handoff/`, `docs/ai_handoff/snapshots/`, and initial `HANDOFF_STATE.md`. Do not analyze source code. Only record repository root, mode, timestamp, and unknown project metadata.

## onboarding-intake

Read inherited documentation first, then validate only critical claims with a small source sample. Write `snapshots/00_onboarding_intake.md`. Update `llm_handoff.md` only when it is missing, obviously stale, or too incomplete to support `task-load`.

## full-build

Run Phase 0-5 from `phase_prompts.md`. Stop after each phase unless the user explicitly said to continue. Never scan the entire repository in one pass. Each phase must name files read, claims supported, unknowns, and recommended next reads.

## task-load

Read `AGENTS.md`, `HANDOFF_STATE.md`, `llm_handoff.md`, task-relevant snapshots, and task-relevant source files. Output a short context summary and task plan. Make no file changes unless the user explicitly asks.

## post-change-refresh

Use git status/diff when available. Read changed files plus directly related files. Update only affected snapshots, regenerate final docs, write `changes/YYYY-MM-DD_post_change_refresh.md`, and update `HANDOFF_STATE.md`.

## drift-check

Compare current git status/diff/recent commits against `HANDOFF_STATE.md`. If git is unavailable, state that limitation and compare only available file timestamps or user-provided change lists. Do not modify files unless explicitly requested.
