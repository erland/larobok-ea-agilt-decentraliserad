# GitHub Actions för läroboken

Den här katalogen ligger i repositoryts rot, på samma nivå som `README.md`.

Workflows och stödskript är införda utifrån det bifogade GitHub Actions-publiceringskitet och
anpassade till lärobokens projektstruktur:

- kapitel: `chapters/`
- exportmetadata: `docs/export-metadata.yaml`
- omslag: `assets/cover/cover.png`
- bygg-/publiceringsstöd: `scripts/` och/eller `publishing/` enligt kitet

Kontrollera repositoryts Actions-flik efter första pushen. Eventuella externa verktyg som
Pandoc/XeLaTeX installeras av workflow-filerna enligt publiceringskitets upplägg.
