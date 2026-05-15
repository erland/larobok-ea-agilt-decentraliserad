# Kapitel 10: Arkitekturdokumentation som gemensamt minne

## Varför detta kapitel finns

I en organisation som lämnar ett mer XLPM-präglat arbetssätt och går mot agil utvecklingslogik förändras även dokumentationens roll. Dokumentation kan inte längre främst vara ett omfattande underlag som produceras inför en beslutspunkt och sedan arkiveras. Den behöver bli ett levande stöd för löpande beslut, lärande och samordning.

Det betyder inte att dokumentation blir mindre viktig. Tvärtom blir den ofta viktigare.

När arkitekturarbetet är decentraliserat finns kunskap utspridd i utvecklingsområden, team, forum, initiativ och vägval. Om denna kunskap bara finns i människors huvuden, i mötesanteckningar eller i lokala presentationer blir organisationen sårbar. Beslut upprepas, gamla vägval glöms bort och nya initiativ riskerar att bygga vidare på ofullständig förståelse.

Detta kapitel handlar om arkitekturdokumentation som ett gemensamt minne: tillräckligt lättviktig för att hållas aktuell, men tillräckligt tydlig för att hjälpa andra att förstå riktning, beroenden, konsekvenser och beslut.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara varför arkitekturdokumentation behövs även i agila arbetssätt
- skilja mellan dokumentation för styrning, lärande och beslut
- beskriva vad som bör dokumenteras centralt respektive lokalt
- använda enkla principer för lättviktig och levande arkitekturdokumentation
- identifiera vanliga dokumentationsfällor i decentraliserade arkitekturorganisationer

## Innan vi börjar

Tidigare kapitel har beskrivit gemensam riktning, arkitekturforum, behovsflöden, beroenden och gemensamma förmågor. Alla dessa delar behöver någon form av minne.

En arkitekturprincip behöver vara synlig. Ett beslut behöver kunna hittas. En målarkitektur behöver kunna förstås även av den som inte var med när den togs fram. En beroendekarta behöver uppdateras när verkligheten förändras. En standard behöver visa när den gäller, varför den finns och hur avsteg hanteras.

Dokumentation är därför inte ett sidospår. Den är en del av arkitekturförmågan.

## Huvudförklaring

### Från leveransdokument till arbetsminne

I ett fasorienterat arbetssätt används dokumentation ofta som leverans. Ett projekt tar fram ett arkitekturunderlag, granskar det, lämnar det vidare och går sedan in i nästa fas. Dokumentet blir ett bevis på att ett steg är genomfört.

I ett agilt och decentraliserat arbetssätt behöver dokumentationen fungera mer som ett arbetsminne. Den ska hjälpa människor att fatta bättre beslut över tid. Den ska inte bara visa vad som beslutades, utan också varför det beslutades, vilka antaganden som låg bakom och när beslutet kan behöva omprövas.

Det innebär en viktig förändring:

- Dokumentation ska inte bara godkännas. Den ska användas.
- Dokumentation ska inte bara beskriva slutresultat. Den ska stödja pågående vägval.
- Dokumentation ska inte bara finnas centralt. Den ska vara tillgänglig där besluten fattas.
- Dokumentation ska inte vara komplett på bekostnad av aktualitet. Den ska vara tillräcklig och levande.

Det gemensamma minnet behöver alltså vara både stabilt och förändringsbart. Stabilt nog för att skapa kontinuitet. Förändringsbart nog för att följa organisationens lärande.

### Vad behöver organisationen komma ihåg?

All arkitekturdokumentation är inte lika viktig. En vanlig fallgrop är att försöka dokumentera allt. Det leder ofta till att ingen orkar hålla materialet uppdaterat. En annan fallgrop är att dokumentera för lite. Då blir organisationen beroende av enskilda personer.

En praktisk utgångspunkt är att dokumentera sådant som andra behöver kunna förstå, återanvända eller ifrågasätta.

I en decentraliserad arkitekturorganisation är fem typer av minne särskilt viktiga.

**1. Gemensam riktning.** Här ingår målarkitektur, principer, guardrails och strategiska avvägningar. Den centrala utvecklingsfunktionen har ofta ett ansvar för att denna dokumentation finns, är begriplig och hålls samman.

**2. Beslut och motiveringar.** Viktiga arkitekturbeslut bör dokumenteras med sammanhang, alternativ, motivering, konsekvenser och eventuella villkor. Det räcker sällan att skriva *beslut: vi väljer lösning A*. Organisationen behöver förstå varför lösning A valdes och när beslutet bör omprövas.

**3. Områdesarkitektur.** Varje utvecklingsområde behöver ha en aktuell bild av sina viktigaste förmågor, informationsobjekt, system, beroenden, vägval och risker. Denna dokumentation behöver ägas lokalt men kunna förstås av andra.

**4. Beroenden och gränssnitt.** När utvecklingsområden påverkar varandra behöver beroenden vara synliga. Det gäller särskilt informationsberoenden, integrationspunkter, gemensamma begrepp och beslut som kräver samordning.

**5. Lärdomar och återkommande mönster.** När organisationen upptäcker vad som fungerar, vad som inte fungerar och vilka mönster som återkommer bör detta fångas. Annars riskerar varje utvecklingsområde att göra samma upptäckt på nytt.

### Central och lokal dokumentation

I en decentraliserad organisation blir frågan inte om dokumentation ska vara central eller lokal. Den behöver vara båda.

Den centrala utvecklingsfunktionen bör normalt ansvara för dokumentation som rör helheten. Det kan vara gemensamma principer, målarkitekturer, beslut med bred påverkan, standarder, övergripande beroendekartor och mallar för hur arkitekturbeslut dokumenteras.

Utvecklingsområdena bör normalt ansvara för dokumentation som rör deras område. Det kan vara områdesarkitektur, lokala beslut, behovsflöden, lokala beroenden, pågående arkitekturrisker och konsekvensbedömningar för initiativ.

Men gränsen är inte absolut. En lokal fråga kan bli gemensam när den påverkar flera områden. En gemensam princip kan behöva konkretiseras lokalt. Därför behöver dokumentationen hänga ihop genom länkar, gemensamma begrepp och tydliga ägarskap.

En enkel regel är:

> Dokumentera där kunskapen uppstår, men gör det möjligt för andra att hitta, förstå och återanvända den.

### Minsta användbara dokumentation

Begreppet minsta användbara dokumentation betyder inte minsta möjliga dokumentation. Det betyder den minsta dokumentation som faktiskt räcker för att stödja nästa beslut, nästa samordning och nästa lärande.

För ett arkitekturbeslut kan det till exempel räcka med:

- vilken fråga beslutet gäller
- vilket beslut som fattades
- vilka alternativ som övervägdes
- varför beslutet fattades
- vilka konsekvenser beslutet får
- vem som äger beslutet
- när beslutet bör följas upp

För en områdesarkitektur kan det räcka med:

- områdets uppdrag och viktigaste verksamhetsförmågor
- centrala informationsobjekt
- viktigaste system och tjänster
- kända beroenden till andra områden
- aktuella arkitekturrisker
- pågående eller planerade större förändringar
- koppling till gemensam riktning

Poängen är att dokumentationen ska vara tydlig nog för att användas, men inte så tung att den bara uppdateras inför revisioner, granskningar eller stora beslutspunkter.

### Dokumentation som del av flödet

Dokumentation blir ofta inaktuell när den hanteras som en separat aktivitet. Någon gör arbetet, beslut fattas, lösningen ändras och först senare kommer frågan: *har vi uppdaterat dokumentationen?*

I ett agilt arbetssätt behöver dokumentation vara en naturlig del av flödet.

När ett behov triageras kan arkitekturell påverkan dokumenteras kort. När ett forum diskuterar en fråga kan beslut och villkor fångas direkt i beslutsloggen. När ett utvecklingsområde förändrar ett viktigt gränssnitt kan beroendekartan uppdateras som en del av arbetet. När en standard införs kan den beskrivas tillsammans med exempel och tillämpningsstöd.

Det betyder att dokumentation inte bör vara slutprodukten. Den bör vara en arbetsprodukt som växer tillsammans med beslutet.

### Ägarskap och livscykel

All viktig arkitekturdokumentation behöver ett tydligt ägarskap. Utan ägare blir dokumentationen snabbt ett arkiv. Ägarskapet behöver inte alltid ligga hos en person, men det måste vara tydligt vilken funktion, vilket forum eller vilket utvecklingsområde som ansvarar för att innehållet är begripligt och aktuellt.

Dokumentation behöver också en livscykel. Vissa delar är långlivade, till exempel övergripande principer. Andra är tillfälliga, till exempel underlag för ett initiativ. Vissa beslut gäller tills vidare. Andra bör omprövas efter en viss period eller när en viss händelse inträffar.

En enkel livscykel kan vara:

1. **Utkast** — innehållet används för diskussion och lärande.
2. **Gällande** — innehållet är beslutat eller etablerat som aktuell riktning.
3. **Under omprövning** — innehållet används fortfarande, men antaganden eller konsekvenser behöver ses över.
4. **Ersatt** — innehållet gäller inte längre, men sparas för historik.
5. **Arkiverat** — innehållet är inte längre aktivt men kan behövas som referens.

Denna livscykel hjälper organisationen att undvika två problem: att gammal dokumentation tolkas som aktuell, och att historiska beslut försvinner så att lärandet går förlorat.

## Exempel: När dokumentationen saknas

Ett utvecklingsområde vill införa en ny lösning för kundkommunikation. Lösningen verkar lokal eftersom den bara påverkar områdets egna processer. Under arbetet visar det sig att lösningen använder kundbegrepp som även förekommer i två andra områden. Den behöver dessutom hämta kontaktuppgifter från en gemensam informationskälla.

Arkitekten i området söker efter tidigare beslut. Det finns presentationer från ett gammalt projekt, några mötesanteckningar och en standard som inte verkar uppdaterad. Ingen kan säkert säga om standarden fortfarande gäller. Den centrala utvecklingsfunktionen minns att frågan diskuterades i ett forum, men beslutet finns inte dokumenterat på ett tydligt sätt.

Resultatet blir att initiativet bromsas. Frågor behöver tas om. Personer behöver intervjuas. Ett nytt forumärende skapas för att reda ut vad organisationen egentligen har beslutat.

I ett bättre fungerande gemensamt minne hade arkitekten kunnat hitta:

- aktuell princip för kundinformation
- beslut om gemensamma kundbegrepp
- ägare till informationsmodellen
- kända beroenden till andra utvecklingsområden
- tidigare avsteg och deras motiveringar
- kontaktväg för att föreslå förändring

Då hade dokumentationen inte varit ett kontrollkrav. Den hade varit ett stöd för snabbare och bättre utveckling.

## Praktiskt arbetssätt: En dokumentationskarta

Ett enkelt sätt att förbättra arkitekturdokumentationen är att skapa en dokumentationskarta. Den behöver inte vara tekniskt avancerad. Den ska svara på fyra frågor:

1. Vilka typer av arkitekturdokumentation har vi?
2. Vem äger respektive typ?
3. Var finns den?
4. När och hur uppdateras den?

En första dokumentationskarta kan till exempel innehålla:

| Dokumentationstyp | Ägare | Placering | Uppdateras när |
|---|---|---|---|
| Arkitekturprinciper | Central utvecklingsfunktion | Gemensam arkitekturplats | Princip ändras eller ny princip beslutas |
| Beslutslogg | Arkitekturforum | Gemensam beslutslogg | Efter varje beslut eller rekommendation |
| Områdesarkitektur | Utvecklingsområde | Områdets arkitekturyta | Vid större behov, initiativ eller kvartalsvis översyn |
| Beroendekarta | Gemensamt forum och berörda områden | Gemensam samverkansyta | När beroenden skapas, ändras eller avvecklas |
| Standarder | Utsedd standardägare | Gemensam arkitekturplats | Vid ändring, avsteg eller återkommande frågor |

Kartan gör inte dokumentationen bättre av sig själv, men den gör ansvar och luckor synliga.

## Vanliga misstag

- **Misstag: Dokumentationen blir en fasleverans.**  
  - Varför det händer: Organisationen är van vid projektmodeller där dokument godkänns vid beslutspunkter.  
  - Hur man undviker det: Koppla dokumentation till löpande beslut, forum, behovsflöden och områdesansvar.

- **Misstag: Allt ska dokumenteras lika detaljerat.**  
  - Varför det händer: Man vill skapa ordning och minska risk, men blandar ihop viktig kunskap med fullständig beskrivning.  
  - Hur man undviker det: Prioritera beslut, riktning, beroenden, konsekvenser och ägarskap.

- **Misstag: Dokumentation saknar ägare.**  
  - Varför det händer: Dokumentationen ses som gemensam, men ingen har ansvar för aktualitet.  
  - Hur man undviker det: Sätt ägare, status och uppföljningspunkt på all viktig arkitekturdokumentation.

- **Misstag: Dokumentationen är korrekt men svår att använda.**  
  - Varför det händer: Den skrivs för granskning snarare än för praktiskt beslutstöd.  
  - Hur man undviker det: Skriv kort, länka vidare, använd tydliga rubriker och förklara varför innehållet spelar roll.

- **Misstag: Historik tas bort för snabbt.**  
  - Varför det händer: Man vill hålla materialet rent och aktuellt.  
  - Hur man undviker det: Skilj mellan aktuell riktning och historiska beslut. Arkivera hellre än att radera viktiga motiveringar.

## Övningar

### Övning 1: Hitta organisationens gemensamma minne

Välj ett aktuellt arkitekturbeslut eller en pågående arkitekturfråga. Undersök:

1. Var finns beslutet eller frågan dokumenterad?
2. Går det att förstå varför vägvalet gjordes?
3. Framgår vem som äger beslutet?
4. Framgår när beslutet ska följas upp eller omprövas?
5. Skulle en ny arkitekt kunna förstå sammanhanget utan att intervjua flera personer?

Skriv ner tre förbättringar som skulle göra dokumentationen mer användbar.

### Övning 2: Skapa en enkel dokumentationskarta

Gör en tabell med fem dokumentationstyper som är viktiga i er arkitekturorganisation. För varje typ, ange ägare, placering och uppdateringstillfälle. Markera sedan vilka rader som är tydliga och vilka som behöver förbättras.

### Fördjupning

Välj en dokumentationstyp, till exempel beslutslogg eller områdesarkitektur. Ta fram en enkel mall på högst en sida. Testa mallen på ett verkligt eller fiktivt exempel och bedöm om den hjälper till att fatta bättre beslut.

## Snabb sammanfattning

- I en decentraliserad arkitekturorganisation behöver dokumentation fungera som gemensamt minne.
- Dokumentationens värde ligger i att stödja beslut, lärande och samordning.
- Den centrala utvecklingsfunktionen bör hålla ihop gemensam riktning, principer, standarder och beslut med bred påverkan.
- Utvecklingsområdena bör äga sin områdesarkitektur och sina lokala vägval.
- Minsta användbara dokumentation är inte minimal dokumentation, utan dokumentation som räcker för nästa beslut och nästa lärande.
- All viktig dokumentation behöver ägare, status och en livscykel.
- Dokumentation bör vara en del av arbetets flöde, inte något som görs i efterhand.

## Quiz/reflektionsfrågor

1. Varför blir arkitekturdokumentation extra viktig när arkitekturarbetet decentraliseras?
2. Vad är skillnaden mellan dokumentation som leverans och dokumentation som arbetsminne?
3. Vilka typer av arkitekturdokumentation bör normalt ägas centralt?
4. Vilka typer bör normalt ägas av utvecklingsområdena?
5. Vad innebär minsta användbara dokumentation?
6. Hur kan en beslutslogg stödja arkitekturellt lärande?
7. Vilka risker uppstår om dokumentation saknar ägare?
8. Hur kan organisationen undvika att gammal dokumentation uppfattas som aktuell riktning?

## Nästa steg

Nästa kapitel handlar om mätning, uppföljning och kvalitet i arkitekturarbetet. Där går vi vidare från frågan *vad behöver organisationen komma ihåg?* till frågan *hur vet vi att arkitekturarbetet faktiskt skapar kvalitet och hjälper organisationen framåt?*
