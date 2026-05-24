# Compatibility Policy

Use this skill across repositories without assuming language, framework, package manager, or agent framework.

## Project detection

Look for current files before making stack claims:

- JavaScript/TypeScript: `package.json`, lockfiles, `tsconfig.json`, framework configs
- Python: `pyproject.toml`, `requirements.txt`, `setup.py`, `Pipfile`, `uv.lock`
- Go: `go.mod`, `go.work`
- Rust: `Cargo.toml`
- Java/Kotlin: `pom.xml`, `build.gradle`, `settings.gradle`
- .NET: `*.sln`, `*.csproj`, `Directory.Build.props`
- Containers: `Dockerfile`, `docker-compose.yml`, compose variants
- General automation: `Makefile`, `justfile`, CI configs, README

Commands from docs are claims until executed. If not executed, say so.

## Monorepos and nested packages

- Identify workspace/package boundaries before deep reads.
- Document package-local entrypoints, tests, and generated directories separately.
- Avoid scanning every package in one phase.
- Mark uninspected packages explicitly.

## Repositories with missing pieces

- No tests: record searched locations and validation alternatives.
- No `AGENTS.md`: `bootstrap` may create the handoff section.
- Existing docs: read them first, then validate critical claims.
- Stale docs: keep useful parts with confidence labels and record conflicts.

## Output compatibility

- Use Markdown for structured handoff files.
- Use single-file HTML with inline CSS and no external resources.
- Prefer path-specific evidence over generalized statements.
- Avoid dependency, build, cache, binary, and generated directories unless explicitly required.
