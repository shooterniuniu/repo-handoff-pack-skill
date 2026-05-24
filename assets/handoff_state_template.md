# Handoff State

## Handoff metadata

- handoff_version:
- last_handoff_commit:
- last_handoff_time:
- last_refresh_mode:
- repository_root:
- primary_language:
- primary_framework:
- confidence_level:

## Completed phases

## Last updated snapshots

## Last changed source files

## Known unknowns

## Detected conflicts

| Claim | Evidence | Conflict | Resolution | Confidence |
| --- | --- | --- | --- | --- |

## Next recommended action

## Resume instruction

Read `AGENTS.md`, this file, and `_local/handoff/<repo>/docs/llm_handoff.md` as the lightweight context index. Then read only task-relevant snapshots, source files, and optional `_local/notes/<repo>/` files when useful or requested. Do not read `_local/env/` for values.

## Refresh policy

- Use task-load before normal coding tasks.
- Use onboarding-intake when joining an unfamiliar repository.
- Use post-change-refresh after code changes.
- Use full-build only when no reliable handoff exists or after major architecture changes.
- Use drift-check before PRs or when unsure whether docs are stale.
