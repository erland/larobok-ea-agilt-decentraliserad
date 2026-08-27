#!/usr/bin/env python3
"""Validera Lärobokskaparens bokprojekt före build/release.

Använder endast Python-standardbiblioteket så att valideringen fungerar direkt
på GitHub-hostade Ubuntu-runners.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]")
REQUIRED_PATHS = (
    "README.md",
    "docs/bokspecifikation.md",
    "docs/kapitelplan.md",
    "docs/pedagogisk-canon.md",
    "docs/terminologi.md",
    "docs/projektstatus.md",
    "docs/export-metadata.yaml",
    "docs/export-guide.md",
    "chapters",
    "assets/cover/cover.png",
    "scripts/build_book.py",
    "publishing/epub.css",
    "publishing/pdf-template.tex",
    "publishing/pdf-filter.lua",
)

REQUIRED_METADATA_KEYS = (
    "title",
    "subtitle",
    "author",
    "language",
    "identifier",
    "version",
    "date",
    "cover_image",
)

def error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)

def parse_top_level_scalars(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1].isspace() or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key, value = key.strip(), value.strip()
        if value and value[0:1] in {"'", '"'} and value[-1:] == value[0]:
            value = value[1:-1]
        values[key] = value
    return values

def parse_chapter_list(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    result: list[str] = []
    in_chapters = False
    for raw in lines:
        if re.match(r"^chapters:\s*$", raw):
            in_chapters = True
            continue
        if in_chapters:
            if raw.startswith("- "):
                result.append(raw[2:].strip().strip("'\""))
                continue
            if raw and not raw[0].isspace():
                break
    return result

def validate_markdown_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            # Strip an optional markdown link title.
            if ' "' in target:
                target = target.split(' "', 1)[0]
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                error(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            error(errors, f"Obligatorisk projektsökväg saknas: {rel}")

    metadata_path = root / "docs/export-metadata.yaml"
    if metadata_path.exists():
        metadata = parse_top_level_scalars(metadata_path)
        for key in REQUIRED_METADATA_KEYS:
            if not metadata.get(key, "").strip():
                error(errors, f"Metadatafält saknas eller är tomt: {key}")
        if metadata.get("language") not in {"sv", "en"}:
            error(errors, "Metadatafältet language måste vara sv eller en.")

        chapter_paths = parse_chapter_list(metadata_path)
        if not chapter_paths:
            error(errors, "Metadata innehåller ingen chapters-lista.")
        else:
            if chapter_paths[0] != "chapters/00-inledning.md":
                error(errors, "Första filen i metadata chapters måste vara chapters/00-inledning.md.")
            seen = set()
            for rel in chapter_paths:
                if rel in seen:
                    error(errors, f"Dubblett i metadata chapters: {rel}")
                seen.add(rel)
                p = root / rel
                if not p.is_file():
                    error(errors, f"Kapitel i metadata saknas: {rel}")
                    continue
                text = p.read_text(encoding="utf-8")
                if not re.search(r"^#\s+\S", text, re.MULTILINE):
                    error(errors, f"Kapitel saknar H1-rubrik: {rel}")

            actual = {p.relative_to(root).as_posix() for p in (root / "chapters").glob("*.md")}
            listed = set(chapter_paths)
            unlisted = sorted(actual - listed)
            if unlisted:
                error(errors, "Markdownkapitel finns men saknas i metadata chapters: " + ", ".join(unlisted))

    # Basic unfinished-marker check in reader-facing chapters only.
    for md in sorted((root / "chapters").glob("*.md")) if (root / "chapters").exists() else []:
        text = md.read_text(encoding="utf-8")
        for marker in MARKERS:
            if marker in text:
                error(errors, f"Ofärdig markör {marker} finns i {md.relative_to(root)}")

    validate_markdown_links(root, errors)

    if errors:
        print(f"Validering misslyckades med {len(errors)} fel.", file=sys.stderr)
        return 1

    print("OK: projektstruktur, metadata, kapitelordning och interna Markdown-länkar är validerade.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
