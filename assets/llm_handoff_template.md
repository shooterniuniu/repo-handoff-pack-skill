# LLM Handoff Index

## Handoff metadata

- handoff_version:
- last_refresh_mode:
- last_handoff_commit:
- last_handoff_time:
- repository_root:
- primary_language:
- primary_framework:
- confidence_level:

## How to resume

Read `AGENTS.md`, `docs/ai_handoff/HANDOFF_STATE.md`, and this file first. Then read only task-relevant snapshots, source files, and optional local/private notes named below.

## Project purpose

## Current state summary

## Source-of-truth notes

| Topic | Current source of truth | Confidence |
| --- | --- | --- |

## Task routes

| Task type | Read first | Then read | Commands to consider | Notes |
| --- | --- | --- | --- | --- |

## Snapshot index

| Snapshot | Topic | When to read | Freshness / confidence |
| --- | --- | --- | --- |

## Key files

| Path | Role | Evidence / notes |
| --- | --- | --- |

## Entrypoints and commands

| Purpose | Command or path | Verified? | Notes |
| --- | --- | --- | --- |

## Detail map

| Detail area | Snapshot / doc to read | Source files to sample | Notes |
| --- | --- | --- | --- |

## Tests and validation

| Need | Read | Command | Verified? |
| --- | --- | --- | --- |

## Optional local/private context

| Path | Use when | Safety notes |
| --- | --- | --- |
| `_local/notes/<repo>/` | Task needs personal study notes or user requests them | Mark as local/private; do not treat as repo truth |
| `_local/env/<repo>/` | Environment setup questions only | Do not read or copy secret values |

## Constraints

## Do-not-touch areas

## Known unknowns

## Detected conflicts

| Claim | Evidence | Conflict | Resolution | Confidence |
| --- | --- | --- | --- | --- |

## Recommended next tasks

## Refresh guidance

- Use `task-load` before coding.
- Use `onboarding-intake` when joining an unfamiliar repository.
- Use `post-change-refresh` after meaningful code changes.
- Use `full-build` only when no reliable handoff exists or after major architecture changes.
- Use `drift-check` before PRs or when stale docs are suspected.
