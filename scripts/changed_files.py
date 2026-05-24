#!/usr/bin/env python3
"""List changed files using git status/diff without reading file contents."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


DEFAULT_EXCLUDES = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "coverage",
    ".next",
    ".turbo",
    ".cache",
    "logs",
    "tmp",
    "vendor",
}


def run_git(root: Path, args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=str(root),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return proc.returncode, proc.stdout, proc.stderr


def excluded(path: str, excludes: set[str]) -> bool:
    normalized = path.replace("\\", "/").strip("/")
    parts = normalized.split("/") if normalized else []
    if parts and (parts[-1] == ".env" or (parts[-1].startswith(".env.") and parts[-1] != ".env.example")):
        return True
    return any(part in excludes for part in parts)


def parse_status_path(line: str) -> str:
    path = line[3:].strip() if len(line) > 3 else line.strip()
    if " -> " in path:
        path = path.split(" -> ", 1)[1].strip()
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository_root", help="Repository root.")
    parser.add_argument("--base", help="Optional base revision for git diff --name-only.")
    parser.add_argument("--exclude", action="append", default=[], help="Additional path component to exclude.")
    args = parser.parse_args()

    root = Path(args.repository_root).resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"repository_root is not a directory: {root}")

    code, _, err = run_git(root, ["rev-parse", "--is-inside-work-tree"])
    if code != 0:
        print(f"[no-git] {err.strip() or 'not a git repository'}")
        return 0

    excludes = DEFAULT_EXCLUDES | set(args.exclude)
    paths: set[str] = set()

    code, stdout, _ = run_git(root, ["status", "--short"])
    if code == 0:
        for line in stdout.splitlines():
            if line.strip():
                paths.add(parse_status_path(line))

    diff_args = ["diff", "--name-only"]
    if args.base:
        diff_args.append(args.base)
    code, stdout, _ = run_git(root, diff_args)
    if code == 0:
        paths.update(line.strip() for line in stdout.splitlines() if line.strip())

    for path in sorted(path for path in paths if path and not excluded(path, excludes)):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
