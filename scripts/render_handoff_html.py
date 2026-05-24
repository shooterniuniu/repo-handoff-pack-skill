#!/usr/bin/env python3
"""Render simple Markdown handoff content to a standalone HTML file."""

from __future__ import annotations

import argparse
import html
import os
import re
from pathlib import Path


STYLE = """
body{margin:0;background:#f7f8fa;color:#17202a;font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.58}
main{width:min(100%,980px);margin:0 auto;padding:42px 24px 80px}
h1{font-size:32px;margin:0 0 18px}
h2{font-size:24px;margin:30px 0 10px;padding-bottom:7px;border-bottom:1px solid #d8dee7}
h3{font-size:18px;margin:22px 0 8px}
p{margin:0 0 12px}
ul,ol{margin:8px 0 16px 24px;padding:0}
li{margin:5px 0}
code{padding:2px 5px;border-radius:4px;background:#e9edf3;font-family:Consolas,"SFMono-Regular",monospace;font-size:.92em}
pre{overflow:auto;padding:16px;border-radius:8px;background:#111827;color:#e5edf7}
pre code{padding:0;background:transparent;color:inherit}
table{width:100%;border-collapse:collapse;margin:14px 0;background:#fff;font-size:14px}
th,td{padding:9px 10px;border:1px solid #d8dee7;text-align:left;vertical-align:top}
th{background:#eef2f7}
@media(max-width:760px){main{padding:28px 16px 52px}table{display:block;overflow-x:auto}}
""".strip()


def inline(text: str) -> str:
    escaped = html.escape(text)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)


def table_to_html(rows: list[str]) -> str:
    header = split_table_row(rows[0])
    body_rows = [split_table_row(row) for row in rows[2:]]
    out = ["<table>", "<thead><tr>"]
    out.extend(f"<th>{inline(cell)}</th>" for cell in header)
    out.append("</tr></thead>")
    if body_rows:
        out.append("<tbody>")
        for row in body_rows:
            out.append("<tr>")
            out.extend(f"<td>{inline(cell)}</td>" for cell in row)
            out.append("</tr>")
        out.append("</tbody>")
    out.append("</table>")
    return "".join(out)


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    in_code = False
    in_ul = False
    in_ol = False
    paragraph: list[str] = []
    index = 0

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{inline(' '.join(paragraph))}</p>")
            paragraph = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            flush_paragraph()
            close_lists()
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append("<pre><code>")
                in_code = True
            index += 1
            continue
        if in_code:
            out.append(html.escape(line))
            index += 1
            continue

        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            close_lists()
            index += 1
            continue

        if (
            stripped.startswith("|")
            and index + 1 < len(lines)
            and is_separator_row(lines[index + 1].strip())
        ):
            flush_paragraph()
            close_lists()
            table_rows = [stripped, lines[index + 1].strip()]
            index += 2
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_rows.append(lines[index].strip())
                index += 1
            out.append(table_to_html(table_rows))
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            close_lists()
            out.append(f"<h1>{inline(stripped[2:])}</h1>")
        elif stripped.startswith("## "):
            flush_paragraph()
            close_lists()
            out.append(f"<h2>{inline(stripped[3:])}</h2>")
        elif stripped.startswith("### "):
            flush_paragraph()
            close_lists()
            out.append(f"<h3>{inline(stripped[4:])}</h3>")
        elif stripped.startswith("- "):
            flush_paragraph()
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(stripped[2:])}</li>")
        elif re.match(r"^\d+\.\s+", stripped):
            flush_paragraph()
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            item_text = re.sub(r"^\d+\.\s+", "", stripped)
            out.append(f"<li>{inline(item_text)}</li>")
        else:
            paragraph.append(stripped)
        index += 1

    flush_paragraph()
    close_lists()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository_root", help="Repository root.")
    parser.add_argument("markdown_path", help="Markdown input path.")
    parser.add_argument(
        "html_path",
        help="HTML output path under _local/handoff/<repo>/docs, or docs/ai_handoff for explicit shared output.",
    )
    args = parser.parse_args()

    root = Path(args.repository_root).resolve()
    md_path = Path(args.markdown_path)
    html_path = Path(args.html_path)
    if not md_path.is_absolute():
        md_path = root / md_path
    if not html_path.is_absolute():
        html_path = root / html_path

    local_root = Path(os.environ.get("REPO_HANDOFF_LOCAL_ROOT", root.parent / "_local"))
    local_handoff_docs = local_root / "handoff" / root.name / "docs"
    shared_handoff_root = root / "docs" / "ai_handoff"
    try:
        resolved_html_path = html_path.resolve()
        try:
            resolved_html_path.relative_to(local_handoff_docs.resolve())
        except ValueError:
            resolved_html_path.relative_to(shared_handoff_root.resolve())
    except ValueError:
        parser.error("html_path must be under _local/handoff/<repo>/docs or docs/ai_handoff")

    body = markdown_to_html(md_path.read_text(encoding="utf-8"))
    document = (
        "<!doctype html>\n"
        "<html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        f"<style>{STYLE}</style></head><body><main>{body}</main></body></html>\n"
    )
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(document, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
