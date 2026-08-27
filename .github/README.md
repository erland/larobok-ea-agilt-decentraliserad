# GitHub Actions

Workflows är anpassade till Lärobokskaparens projektstruktur.

- `01-validate.yml`: validerar struktur, metadata, kapitelordning och interna Markdown-länkar.
- `02-build-preview.yml`: manuell preview-build av EPUB och PDF som GitHub Actions-artifact.
- `03-release.yml`: bygger EPUB/PDF och bifogar dem till en GitHub Release när en `v*`-tagg pushas.

Kanoniska sökvägar:
- `chapters/`
- `docs/export-metadata.yaml`
- `assets/cover/cover.png`
