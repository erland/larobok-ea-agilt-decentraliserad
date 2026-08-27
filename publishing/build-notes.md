# Build notes

Markdown är kanonisk källa. Kapitelnoteringar exporteras inte.

## EPUB-export revision 109

- Exportdatum: 2026-08-05
- Indatarevision: 108
- Exportfil: `glodhjartats-val-r0109.epub`
- Format: EPUB 3
- Verktyg: Pandoc 3.1.11.1
- Innehåll: kapitel 1–30 i numerisk ordning
- Omslag: `omslag/assets/cover/cover.png`
- Titel: Glödhjärtats val
- Serie: De fyra elementens väktare
- Författare: Erland Lindmark
- Språk: sv-SE
- Navigering: Pandoc-TOC med djup 1; `nav.xhtml` kvar i manifestet och satt till `linear="no"`
- Synlig TOC-sida: nej
- Titelsida: separat, inte med i TOC
- Kapitelstart: nummer och rubrik på två centrerade, kompakta rader
- Brödtext: bokmässiga stycken med indrag, 1,52 radavstånd och läsbar serif-stack utan inbäddade fontfiler
- Kapitelrubriker: inga regler med `page-break-before: always` eller `break-before: page`
- Efterbearbetning: `publishing/fix-epub-after-pandoc.py`
- EPUB SHA-256: `04c0b20998a742c56bd9d3d764d43e5e67ed768dfd255acd74a3ae7d3dfd0cc6`

## Kontroll

- 30 kapitel inkluderade
- Första kapitel: 1. Hammarslagen
- Sista kapitel: 30. Arvingen
- Saknade kapitelnummer: inga
- TOC-poster för kapitel: 30
- Delade kapitelrubriker i XHTML: 30
- Råa markdownmarkörer hittades inte
- Omslag finns
- `mimetype` ligger först och är okomprimerad
- EPUBCheck fanns inte installerat i miljön; strukturen kontrollerades direkt i EPUB-arkivet

## EPUB-export revision 110

- Exportdatum: 2026-08-05
- Indatarevision: 109
- Exportfil: `glodhjartats-val-r0110-luftiga-stycken.epub`
- Verktyg: Pandoc 3.1.11.1
- Kapitel: 1–30
- Styckeformat: inget förstahandsindrag
- Styckeavstånd: 0,55 em efter varje stycke
- Vänsterkant: samtliga stycken börjar vid samma vänstermarginal
- Radavstånd: 1,52
- Omslag, titelsida, kapitelrubriker och navigerings-TOC: oförändrade från föregående professionella EPUB
- EPUB SHA-256: `a402b4754abdceaf8830d06959006aa1b6881513cf7dbe8fc12274bba2d678d9`
- Kontroll: 30 kapitelrubriker, nav `linear="no"`, inga förstahandsindrag i EPUB-CSS

## EPUB-export revision 112

- Exportdatum: 2026-08-05
- Indatarevision: 111
- Exportfil: `glodhjartats-val-r0112.epub`
- Verktyg: Pandoc 3.1.11.1
- Kapitel: 1–30
- Titelsida: den dubblerade H1-titeln ovanför den formgivna titelsidan har tagits bort
- TOC: titelsidan ingår inte; endast kapitel 1–30 visas
- Kapitelnummer: minskat med 30 procent från 1,45 em till 1,015 em
- Kapitelrubrik: minskat med 30 procent från 1,30 em till 0,91 em
- Styckeformat: vänsterställda stycken utan indrag och med 0,55 em mellanrum
- Omslag: `omslag/assets/cover/cover.png`
- EPUB SHA-256: `13d57a15fe3f481f968c6b079e25ba4748e5ed412c91e4094f2105b77e16766e`
- Kontroll: 30 kapitelposter i TOC, ingen titelsidepost, 30 delade kapitelrubriker, duplicerad titelside-H1 borttagen, `mimetype` först och okomprimerad

## Reproducerbart GitHub-bygge – revision 113

- Lokalt byggscript: `scripts/build_book.py`
- Deterministisk validering: `scripts/validate_project.py`
- Låst Pandoc-version i GitHub Actions: 3.1.11.1
- EPUB-byggkommando: `python3 scripts/build_book.py --output-dir <utdatakatalog>`
- Kapitelkälla: `kapitel/kapitel-01.md`–`kapitel/kapitel-30.md`
- EPUB-efterbearbetning: `publishing/fix-epub-after-pandoc.py`
- PDF: inte aktiverad i CI eftersom `publishing/pdf-template.tex` ännu är en platshållare
- Preview-exporter lagras som tillfälliga GitHub Actions-artifacts; permanenta versioner skapas via GitHub Releases

## PDF-layout och automatiserat dubbelbygge – revision 114

- PDF-mall: `publishing/pdf-template.tex`
- PDF-filter: `publishing/pdf-filter.lua`
- Sidformat: 140 × 216 mm
- Brödtext: TeX Gyre Pagella, 11 pt, 1,28 radavstånd
- Stycken: vänsterställda utan förstahandsindrag, 0,55 em styckeavstånd
- Kapitelstart: nummer och rubrik på två centrerade kompakta rader
- Omslag: helsida först i PDF
- Titelsida: separat och utan dubblerad titel
- Innehållsförteckning: synlig och klickbar, endast kapitel
- Byggmotor: Pandoc 3.1.11.1 + XeLaTeX
- GitHub Build Preview och Release bygger nu både EPUB och PDF

## Separata preview-artifacts – revision 115

- Build Preview bygger fortsatt EPUB och PDF i samma jobb.
- EPUB publiceras som artifact `glodhjartats-val-preview-epub`.
- PDF publiceras som artifact `glodhjartats-val-preview-pdf`.
- Retention: 7 dagar för båda.
- Release-flödet är oförändrat och publicerar EPUB och PDF som separata GitHub Release assets.

## GitHub fontfix – revision 116

- GitHub-runnern hade XeLaTeX men saknade TeX Gyre Pagella.
- Build Preview och Release installerar nu `fonts-texgyre`.
- `fc-cache -f` körs efter installationen.
- En `fc-list`-kontroll verifierar fonten före PDF-bygget.
- `scripts/build_book.py` gör samma font-preflight vid lokala och CI-byggen.
- PDF-layout och kapiteltexter är oförändrade.

## XeLaTeX fontfil-fix – revision 117

- Orsak: `fc-list` kunde se TeX Gyre Pagella medan XeLaTeX/fontspec ändå inte kunde lösa familjenamnet `TeXGyrePagella`.
- PDF-bygget söker nu de fyra exakta OTF-filerna `texgyrepagella-regular.otf`, `-bold.otf`, `-italic.otf` och `-bolditalic.otf`.
- När OTF-filerna finns skickas deras katalog explicit till Pandoc/PDF-mallen.
- GitHub Preview och Release verifierar nu att den faktiska regular-OTF-filen finns efter installationen.
- Lokal fallback till registrerat familjenamn finns kvar för miljöer där OTF-filerna ligger utanför de vanliga Debian/Ubuntu-sökvägarna.
- Kapiteltexter och PDF-layout är oförändrade.

## fontspec Path-fix – revision 118

- r117 hittade korrekt TeX Gyre Pagellas OTF-katalog men använde en fontspec-kombination som fortfarande försökte slå upp filnamnet.
- PDF-mallen använder nu verifierad fontspec-syntax: `Path=...`, `Extension=.otf` samt `UprightFont/BoldFont/ItalicFont/BoldItalicFont` utan filändelse.
- Syntaxen har testats separat med XeLaTeX och riktiga OpenType-filer.
- GitHub-workflowets `fonts-texgyre`-installation och kontroll av den faktiska OTF-filen behålls.
- Kapiteltexter och övrig PDF-layout är oförändrade.

## Gemensamt preview-paket – revision 119

- Build Preview bygger fortsatt både EPUB och PDF i samma jobb.
- Båda filerna publiceras nu i ett enda GitHub Actions-artifact: `glodhjartats-val-preview`.
- GitHub levererar artifactet som en nedladdnings-zip med både `.epub` och `.pdf`.
- Ingen extra zip skapas inne i artifactet.
- Retention: 7 dagar.
- Release-flödet är oförändrat och publicerar EPUB och PDF som separata GitHub Release assets.

