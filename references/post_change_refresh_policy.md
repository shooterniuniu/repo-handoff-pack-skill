# Post-Change Refresh Policy

Use for `post-change-refresh` after meaningful code changes.

## Step 1: Identify changes

Prefer:

```text
git status --short
git diff --name-only
git diff --stat
```

If git metadata is unavailable, state that limitation and ask for or use the user's changed-file list. Do not guess changed business files from a full repository scan.

## Step 2: Classify changed files

| Category | Common affected snapshots |
| --- | --- |
| entrypoints/framework/config | `01_framework_map.md` |
| agent/router/workflow/lifecycle | `02_agent_design.md` |
| chain/tools/integrations/callbacks | `03_chain_and_tools.md` |
| schema/types/models | `04_schema_datastore_prompt.md` |
| DataStore/state/memory | `04_schema_datastore_prompt.md` |
| prompts/templates/instructions | `04_schema_datastore_prompt.md` |
| tests/fixtures/validation | `05_tests_and_risks.md` |
| docs-only | usually state/change report only |

## Step 3: Read narrowly

Read changed files, directly related files, affected snapshots, and final handoff docs when regenerating them. Do not rerun `full-build` unless the architecture changed so broadly that affected sections cannot be isolated.

## Step 4: Update affected snapshots

Update only affected `docs/ai_handoff/snapshots/*.md`. Preserve unchanged sections where the evidence still applies. Add conflict records when docs and code disagree.

## Step 5: Regenerate final docs

Regenerate:

- `docs/ai_handoff/llm_handoff.md`
- `docs/ai_handoff/llm_handoff.html`
- `docs/ai_handoff/human_overview.html`

Final docs should synthesize snapshots; source files should only be reread for specific gaps.

## Step 6: Record state and change report

Write `docs/ai_handoff/changes/YYYY-MM-DD_post_change_refresh.md` with changed files, files read, affected snapshots, summary, tests/validation, conflicts, unknowns, and next action. Update `HANDOFF_STATE.md` metadata, last changed source files, last updated snapshots, conflicts, and resume instruction.
