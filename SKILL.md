---
name: repo-handoff-pack
description: Repo Handoff Lifecycle Skill v2. Use for repository handoff lifecycle tasks: bootstrap docs/ai_handoff, intake inherited handoff docs, run staged full-build documentation, load lightweight context indexes before coding, refresh handoff docs after code changes, check documentation drift, or manage local/private _local workspace context. Produces human-readable and LLM-oriented handoff artifacts without modifying business code during documentation-only work.
---

# Repo Handoff Lifecycle Skill v2

Use this skill to manage repository handoff memory across the project lifecycle. The memory directory is `docs/ai_handoff/`; the skill method lives in `.agents/skills/repo-handoff-pack/`.

Choose one mode before taking action. If the user did not name a mode, infer the narrowest mode that satisfies the request and state it briefly. Documentation-only modes must not modify business code.

## Core rules

- Do not modify business code during documentation-only handoff tasks.
- Write generated handoff artifacts only under `docs/ai_handoff/`.
- Write skill workflow resources only under `.agents/skills/repo-handoff-pack/`.
- Do not write generated documentation into `src/`, `app/`, `lib/`, `server/`, `packages/`, `services/`, `components/`, or other business-code directories.
- Do not scan an entire repository in one pass.
- Keep `docs/ai_handoff/llm_handoff.md` as a lightweight context index; put detailed evidence in snapshots and load it on demand.
- Treat sibling `_local/` workspaces as optional local/private context. Do not commit them, and never copy secrets or raw environment values into handoff artifacts.
- Always write intermediate snapshots before final synthesis in `full-build`.
- Mark uncertainty explicitly.
- Stop after each staged phase unless the user explicitly asks to continue.
- Do not invent architecture details, tool behavior, schemas, prompts, data flows, commands, or test coverage.

## Mode selection

- Missing handoff structure: use `bootstrap`.
- Unfamiliar repository or inherited handoff docs: use `onboarding-intake`.
- No reliable handoff exists: use `full-build`.
- Normal coding task starting point: use `task-load`.
- Code already changed and docs need refresh: use `post-change-refresh`.
- Unsure whether docs are stale: use `drift-check`.

When in doubt between `onboarding-intake` and `full-build`, start with `onboarding-intake` if any useful inherited documentation exists. When in doubt between `drift-check` and `post-change-refresh`, start with `drift-check` unless the user explicitly asked to update files.

## Modes

### bootstrap

Use when a repository does not yet have a handoff structure.

Purpose:

- Create or update `AGENTS.md` handoff workflow section.
- Create `docs/ai_handoff/` structure.
- Create initial `HANDOFF_STATE.md`.
- Do not analyze source code.

Outputs:

- `AGENTS.md` handoff section.
- `docs/ai_handoff/HANDOFF_STATE.md`.
- `docs/ai_handoff/WORKFLOW.md` when useful.
- `docs/ai_handoff/snapshots/` directory.

### onboarding-intake

Use when entering an unfamiliar repository or reading someone else's handoff documents.

Purpose:

- Read existing handoff-like documents.
- Read README, AGENTS.md, architecture docs, runbooks, ADRs, existing `docs/ai_handoff` files, and other project documentation.
- Summarize inherited context.
- Validate only critical claims against a small number of source files.
- Mark conflicts and uncertainty.
- Do not rewrite the whole repository documentation blindly.

Outputs:

- `docs/ai_handoff/snapshots/00_onboarding_intake.md`.
- `docs/ai_handoff/llm_handoff.md` as a lightweight index if missing or stale.
- `docs/ai_handoff/HANDOFF_STATE.md`.

### full-build

Use when a repository does not have reliable handoff documentation.

Purpose:

- Run the staged Phase 0-5 workflow.
- Write snapshots before final synthesis.
- Stop after each phase unless explicitly told to continue.
- Do not scan the entire repository in one pass.

Outputs:

- `docs/ai_handoff/snapshots/00_repo_inventory.md`.
- `docs/ai_handoff/snapshots/01_framework_map.md`.
- `docs/ai_handoff/snapshots/02_agent_design.md`.
- `docs/ai_handoff/snapshots/03_chain_and_tools.md`.
- `docs/ai_handoff/snapshots/04_schema_datastore_prompt.md`.
- `docs/ai_handoff/snapshots/05_tests_and_risks.md`.
- `docs/ai_handoff/human_overview.html`.
- `docs/ai_handoff/llm_handoff.md` as a lightweight index and routing map.
- `docs/ai_handoff/llm_handoff.html`.
- `docs/ai_handoff/HANDOFF_STATE.md`.

### task-load

Use at the beginning of a new coding task.

Purpose:

- Load project context without regenerating documentation.
- Read `AGENTS.md`.
- Read `docs/ai_handoff/HANDOFF_STATE.md`.
- Read `docs/ai_handoff/llm_handoff.md` as the context index.
- Read only task-relevant snapshots named by the index.
- Read `_local/notes/<repo>/` only when useful for the task or explicitly requested, and mark it local/private.
- Read only task-relevant source files.

Output:

- No file changes unless user explicitly asks.
- A short context summary and task plan.

### post-change-refresh

Use after code has changed.

Purpose:

- Use git status and git diff to identify changed files.
- Read only changed files and directly related files.
- Determine which handoff snapshots are affected.
- Update only affected snapshots.
- Regenerate final human and LLM handoff documents.
- Update `HANDOFF_STATE.md`.

Outputs:

- Updated affected `docs/ai_handoff/snapshots/*.md`.
- `docs/ai_handoff/llm_handoff.md`.
- `docs/ai_handoff/llm_handoff.html`.
- `docs/ai_handoff/human_overview.html`.
- `docs/ai_handoff/HANDOFF_STATE.md`.
- `docs/ai_handoff/changes/YYYY-MM-DD_post_change_refresh.md`.

### drift-check

Use to check whether handoff documents are stale.

Purpose:

- Compare current git status / git diff / recent commits against `HANDOFF_STATE.md`.
- Identify likely stale sections.
- Do not modify files unless explicitly requested.
- Recommend `bootstrap`, `onboarding-intake`, `full-build`, or `post-change-refresh`.

Output:

- A concise drift report with stale areas, evidence, and recommended mode.

## Source-of-truth priority

When documentation conflicts with code, use this order:

1. Current source code
2. Current `AGENTS.md`
3. Current `docs/ai_handoff/llm_handoff.md`
4. Current `docs/ai_handoff/snapshots/`
5. README and other project docs
6. Imported or inherited handoff documents
7. Local/private notes, when explicitly read for the task
8. User-provided natural language context

Always mark conflicts explicitly:

- Claim
- Evidence
- Conflict
- Resolution
- Confidence

Never invent architecture details, tool behavior, schemas, prompts, or data flow.

## Compatibility rules

- Do not assume a specific language, framework, package manager, or agent framework.
- Detect project type from files such as `package.json`, `pyproject.toml`, `requirements.txt`, `go.mod`, `Cargo.toml`, `pom.xml`, `build.gradle`, `Makefile`, `Dockerfile`, `docker-compose.yml`, and README.
- Support monorepos.
- Support nested packages.
- Support repositories with no tests.
- Support repositories with no `AGENTS.md`.
- Support repositories with existing documentation.
- Support repositories with stale documentation.
- Use Markdown and single-file HTML outputs.
- HTML must use inline CSS and no external network resources.
- Prefer path-specific evidence.
- Avoid reading dependency, build, cache, binary, and generated directories.

## Handoff state contract

Every `docs/ai_handoff/HANDOFF_STATE.md` should include:

```markdown
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

## Next recommended action

## Resume instruction

## Refresh policy

- Use task-load before normal coding tasks.
- Use onboarding-intake when joining an unfamiliar repository.
- Use post-change-refresh after code changes.
- Use full-build only when no reliable handoff exists or after major architecture changes.
- Use drift-check before PRs or when unsure whether docs are stale.
```

Use `.agents/skills/repo-handoff-pack/assets/handoff_state_template.md` when creating or upgrading the state file.

## Excluded paths

Avoid these paths unless the user explicitly requires them:

- `node_modules/`
- `.git/`
- `dist/`
- `build/`
- `coverage/`
- `.next/`
- `.turbo/`
- `.cache/`
- `logs/`
- `tmp/`
- `vendor/`
- `.env`
- `.env.*` except safe examples such as `.env.example`
- `_local/` except task-relevant `_local/notes/<repo>/` when explicitly useful
- generated files
- large binary files
- large datasets

Treat generated dependency and build directories as opaque even if they contain source-like files. Record that they were excluded instead of summarizing their contents.

## Resource guide

Load references only when needed:

- `references/lifecycle_modes.md`: mode selection and mode-specific steps.
- `references/onboarding_intake_policy.md`: inherited docs intake and conflict handling.
- `references/post_change_refresh_policy.md`: incremental refresh after code changes.
- `references/compatibility_policy.md`: language/framework/monorepo compatibility.
- `references/source_of_truth_policy.md`: evidence priority and conflict format.
- `references/output_contract.md`: required outputs and section contracts.
- `references/phase_prompts.md`: full-build Phase 0-5 prompts.
- `references/progressive_disclosure_policy.md`: lightweight LLM index and on-demand snapshot loading.
- `references/local_workspace_policy.md`: optional `_local/` workspace layout, local notes, env safety, and local git excludes.

Use assets for output generation:

- `assets/human_overview_template.html`
- `assets/llm_handoff_template.md`
- `assets/onboarding_intake_template.md`
- `assets/post_change_refresh_template.md`
- `assets/handoff_state_template.md`

Optional scripts:

- `scripts/collect_tree.py`: dependency-light tree inventory helper.
- `scripts/changed_files.py`: git changed-files helper.
- `scripts/render_handoff_html.py`: Markdown-to-single-file-HTML helper.

The skill must remain usable without running scripts.

Scripts are helpers, not authorities. Validate any important script output against the repository when it affects a handoff claim.

## Verification

Before finishing a handoff task:

- Verify required output files exist.
- Verify no business code was modified during documentation-only work.
- Verify excluded directories were not scanned deeply.
- Verify `HANDOFF_STATE.md` was updated when files changed.
- Verify unknowns and conflicts are explicit.
- Do not claim tests pass unless a fresh test command was run and checked.
