# Full-Build Phase Prompts

Use these prompts for `full-build`. Stop after each phase unless the user explicitly asks to continue.

## Phase 0: Inventory

Inspect only directory tree, top-level README-like files, top-level configs, manifests, and agent instruction files.

Output `docs/ai_handoff/snapshots/00_repo_inventory.md` with:

- repository shape and excluded paths
- detected language/framework/package hints
- candidate entrypoints
- candidate agent/workflow/tool/schema/state/prompt/test files
- monorepo or nested-package signals
- optional sibling `_local/` presence, without reading private contents
- Phase 1 recommended reads
- unknowns

## Phase 1: Framework map

Read only Phase 0 recommended files unless a small config file is clearly necessary.

Output `docs/ai_handoff/snapshots/01_framework_map.md` with:

- stack and framework structure
- package/workspace boundaries
- entrypoints and commands found
- build/test/run commands, marked unverified unless run
- key configs
- Phase 2 recommended reads
- unknowns

## Phase 2: Agent design

Read relevant files about agent, router, workflow, graph, state, memory, prompt, model configuration, and lifecycle hooks.

Output `docs/ai_handoff/snapshots/02_agent_design.md` with:

- roles and lifecycle
- inputs and outputs
- routing/workflow behavior
- model and prompt relationships
- state/memory boundaries
- constraints and safety rules
- key evidence paths
- unknowns

## Phase 3: Chain and tools

Read relevant files about tools, registries, function calling, chains, callbacks, integrations, side effects, and error paths.

Output `docs/ai_handoff/snapshots/03_chain_and_tools.md` with:

- end-to-end request chain
- tool registry and caller map
- per-tool inputs, outputs, side effects, errors, and test clues
- external integration boundaries
- unknowns

## Phase 4: Schema, DataStore, prompt, tests

Read only files identified by prior snapshots.

Outputs:

- `docs/ai_handoff/snapshots/04_schema_datastore_prompt.md`
- `docs/ai_handoff/snapshots/05_tests_and_risks.md`

Include schema/model relationships, state persistence, memory, prompt templates and variables, data flow, tests, validation commands, coverage judgment, risks, and maintenance recommendations.

## Phase 5: Final synthesis

Use snapshots as the primary source.

Outputs:

- `docs/ai_handoff/human_overview.html`
- `docs/ai_handoff/llm_handoff.md` as a lightweight context index and task routing map
- `docs/ai_handoff/llm_handoff.html`
- updated `docs/ai_handoff/HANDOFF_STATE.md`

Only re-read source files when snapshots identify a specific critical gap. Final docs must be useful to both humans and future LLM agents. Keep detailed explanations in snapshots and the human overview; keep the LLM handoff concise enough to guide on-demand reads.
