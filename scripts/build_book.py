#!/usr/bin/env python3
"""Bygg EPUB och PDF från Lärobokskaparens kanoniska Markdown-kapitel."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

PANDOC_VERSION = "3.1.11.1"
XHTML_NS = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF_NS = "http://www.idpf.org/2007/opf"

def top_level_scalars(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    pending_key = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  ") and pending_key and ":" not in raw:
            values[pending_key] = (values.get(pending_key, "") + " " + raw.strip()).strip()
            continue
        pending_key = None
        if raw[:1].isspace() or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key, value = key.strip(), value.strip()
        if value and value[0:1] in {"'", '"'} and value[-1:] == value[0]:
            value = value[1:-1]
        values[key] = value
        pending_key = key
    return values

def chapter_paths(path: Path, root: Path) -> list[Path]:
    lines = path.read_text(encoding="utf-8").splitlines()
    result: list[Path] = []
    active = False
    for raw in lines:
        if re.match(r"^chapters:\s*$", raw):
            active = True
            continue
        if active:
            if raw.startswith("- "):
                result.append(root / raw[2:].strip().strip("'\""))
                continue
            if raw and not raw[0].isspace():
                break
    return result

def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")

def pandoc_version() -> str:
    result = subprocess.run(["pandoc", "--version"], text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError("Pandoc finns inte i PATH.")
    first = result.stdout.splitlines()[0]
    match = re.search(r"pandoc\s+([0-9][^\s]*)", first)
    return match.group(1) if match else first

def validate_epub(path: Path, expected_docs: int) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            raise RuntimeError("EPUB-fel: mimetype ligger inte först.")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise RuntimeError("EPUB-fel: mimetype är komprimerad.")
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = container.find(".//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile")
        if rootfile is None:
            raise RuntimeError("EPUB-fel: OPF-root saknas.")
        opf_name = rootfile.attrib["full-path"]
        opf = ET.fromstring(archive.read(opf_name))
        ns = {"opf": OPF_NS}
        manifest = opf.find("opf:manifest", ns)
        if manifest is None:
            raise RuntimeError("EPUB-fel: manifest saknas.")
        nav_item = next((i for i in manifest.findall("opf:item", ns)
                         if "nav" in i.attrib.get("properties", "").split()), None)
        if nav_item is None:
            raise RuntimeError("EPUB-fel: navigeringsdokument saknas.")
        nav_path = (Path(opf_name).parent / nav_item.attrib["href"]).as_posix()
        nav_root = ET.fromstring(archive.read(nav_path))
        nav_ns = {"x": XHTML_NS, "epub": EPUB_NS}
        anchors = nav_root.findall(".//x:nav[@epub:type='toc']//x:a", nav_ns)
        if len(anchors) < expected_docs:
            raise RuntimeError(
                f"EPUB-fel: TOC har bara {len(anchors)} poster; minst {expected_docs} väntades."
            )

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--name", default="")
    ap.add_argument("--formats", default="epub,pdf")
    ap.add_argument("--allow-pandoc-version-mismatch", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir).resolve()

    validation = subprocess.run([sys.executable, "scripts/validate_project.py", "."], cwd=root)
    if validation.returncode:
        return validation.returncode

    version = pandoc_version()
    if version != PANDOC_VERSION and not args.allow_pandoc_version_mismatch:
        print(f"ERROR: Pandoc {PANDOC_VERSION} krävs; hittade {version}.", file=sys.stderr)
        return 2

    metadata_path = root / "docs/export-metadata.yaml"
    metadata = top_level_scalars(metadata_path)
    chapters = chapter_paths(metadata_path, root)
    title = metadata["title"]
    author = metadata["author"]
    subtitle = metadata.get("subtitle", "")
    base_name = re.sub(r"\.(epub|pdf)$", "", args.name or slugify(title), flags=re.I)
    formats = [x.strip().lower() for x in args.formats.split(",") if x.strip()]
    if not formats or set(formats) - {"epub", "pdf"}:
        print("ERROR: --formats måste innehålla epub och/eller pdf.", file=sys.stderr)
        return 2

    output_dir.mkdir(parents=True, exist_ok=True)
    cover = root / metadata.get("cover_image", "assets/cover/cover.png")

    if "epub" in formats:
        epub = output_dir / f"{base_name}.epub"
        cmd = [
            "pandoc", *map(str, chapters),
            "--from=markdown", "--to=epub3",
            "--output", str(epub),
            "--metadata-file", str(metadata_path),
            "--css", str(root/"publishing/epub.css"),
            "--epub-cover-image", str(cover),
            "--toc", "--toc-depth=2", "--split-level=1",
        ]
        subprocess.run(cmd, cwd=root, check=True)
        validate_epub(epub, len(chapters))
        print(f"OK: EPUB skapad och verifierad: {epub}")

    if "pdf" in formats:
        pdf = output_dir / f"{base_name}.pdf"
        if shutil.which("xelatex") is None:
            print("ERROR: xelatex krävs för PDF-bygget.", file=sys.stderr)
            return 2
        cmd = [
            "pandoc", *map(str, chapters),
            "--from=markdown", "--to=pdf",
            "--pdf-engine=xelatex",
            "--output", str(pdf),
            "--metadata-file", str(metadata_path),
            "--template", str(root/"publishing/pdf-template.tex"),
            "--lua-filter", str(root/"publishing/pdf-filter.lua"),
            "--variable", f"cover-image={cover.as_posix()}",
            "--toc", "--toc-depth=1",
            "--top-level-division=chapter",
        ]
        subprocess.run(cmd, cwd=root, check=True)
        if not pdf.exists() or pdf.stat().st_size < 10_000:
            print("ERROR: PDF-bygget gav ingen giltig PDF-fil.", file=sys.stderr)
            return 2
        print(f"OK: PDF skapad: {pdf}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
