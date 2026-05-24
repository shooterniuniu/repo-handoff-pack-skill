# Source-of-Truth Policy

Use when claims conflict, evidence is weak, or confidence is unclear.

## Priority

1. Current source code
2. Current `AGENTS.md`
3. Current `docs/ai_handoff/llm_handoff.md`
4. Current `docs/ai_handoff/snapshots/`
5. README and other project docs
6. Imported or inherited handoff documents
7. Local/private notes, when explicitly read for the task
8. User-provided natural language context

Local/private notes are personal context, not repository truth. Use them as leads, questions, or task memory. Do not let them override current source code, current agent instructions, or committed handoff artifacts.

## Conflict record

Use this structure:

- Claim:
- Evidence:
- Conflict:
- Resolution:
- Confidence:

## Confidence labels

- high: directly supported by current source, current workflow instructions, or verified command output
- medium: supported by current docs and consistent with sampled source
- low: inherited, inferred, stale, or not validated
- local/private: from `_local/notes` and not committed project truth

## Resolution rules

- Prefer current code over older documentation.
- Prefer current `AGENTS.md` for workflow constraints.
- Treat README commands as unverified until run.
- Treat `_local/notes` claims as private and unverified until supported by current code or committed docs.
- Never use `_local/env` values as handoff evidence, and never copy raw secrets into generated artifacts.
- When source code and docs disagree, state the conflict rather than merging both into a vague summary.
- Never invent architecture details, tool behavior, schemas, prompts, or data flow.
