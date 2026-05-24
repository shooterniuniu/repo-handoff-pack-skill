# Source-of-Truth Policy

Use when claims conflict, evidence is weak, or confidence is unclear.

## Priority

1. Current source code
2. Current `AGENTS.md`
3. Current `docs/ai_handoff/llm_handoff.md`
4. Current `docs/ai_handoff/snapshots/`
5. README and other project docs
6. Imported or inherited handoff documents
7. User-provided natural language context

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

## Resolution rules

- Prefer current code over older documentation.
- Prefer current `AGENTS.md` for workflow constraints.
- Treat README commands as unverified until run.
- When source code and docs disagree, state the conflict rather than merging both into a vague summary.
- Never invent architecture details, tool behavior, schemas, prompts, or data flow.
