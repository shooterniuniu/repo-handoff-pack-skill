#!/usr/bin/env python3
"""Print a shallow repository tree while avoiding generated/dependency paths."""

from __future__ import annotations

import argparse
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
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}


def is_excluded(path: Path, root: Path, excludes: set[str]) -> bool:
    try:
        rel_parts = path.relative_to(root).parts
    except ValueError:
        rel_parts = path.parts
    if path.name == ".env" or (path.name.startswith(".env.") and path.name != ".env.example"):
        return True
    return any(part in excludes for part in rel_parts)


def iter_tree(root: Path, max_depth: int, excludes: set[str], max_entries: int) -> list[str]:
    lines: list[str] = []

    def visit(path: Path, depth: int, prefix: str) -> None:
        if len(lines) >= max_entries:
            return
        if depth > max_depth:
            return
        try:
            children = sorted(path.iterdir(), key=lambda item: (not item.is_dir(), item.name.lower()))
        except OSError as exc:
            lines.append(f"{prefix}[unreadable: {exc}]")
            return

        for child in children:
            if len(lines) >= max_entries:
                return
            if is_excluded(child, root, excludes):
                continue
            symlink = " ->" if child.is_symlink() else ""
            marker = "/" if child.is_dir() and not child.is_symlink() else ""
            lines.append(f"{prefix}{child.name}{marker}{symlink}")
            if child.is_dir() and not child.is_symlink():
                visit(child, depth + 1, prefix + "  ")

    visit(root, 0, "")
    if len(lines) >= max_entries:
        lines.append(f"[truncated after {max_entries} entries]")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository_root", help="Repository root to inspect.")
    parser.add_argument("--max-depth", type=int, default=2, help="Maximum directory depth. Default: 2.")
    parser.add_argument("--max-entries", type=int, default=500, help="Maximum entries to print. Default: 500.")
    parser.add_argument("--exclude", action="append", default=[], help="Additional path name to exclude.")
    args = parser.parse_args()

    root = Path(args.repository_root).resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"repository_root is not a directory: {root}")
    excludes = DEFAULT_EXCLUDES | set(args.exclude)
    for line in iter_tree(root, args.max_depth, excludes, args.max_entries):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
