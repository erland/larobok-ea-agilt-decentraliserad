# Kapitel 3: Den centrala utvecklingsfunktionens nya uppdrag

## Varför detta kapitel finns

I de två första kapitlen har vi beskrivit två viktiga förändringar. För det första kan enterprise arkitektur inte längre förstås som något som huvudsakligen ägs centralt. För det andra räcker det inte att fortsätta arbeta enligt en XLPM-präglad faslogik om organisationen samtidigt vill röra sig mot mer agila arbetssätt.

Det leder till en central fråga: vad ska den centrala utvecklingsfunktionen då göra?

I en decentraliserad arkitekturorganisation kan den centrala funktionen lätt hamna i ett av två ytterlägen. Det ena är att försöka fortsätta styra genom granskning, godkännande och detaljerade beslut. Då blir funktionen snabbt en flaskhals. Det andra är att backa undan för mycket och lämna varje utvecklingsområde att tolka riktning, kvalitet och beroenden på egen hand. Då riskerar organisationen att tappa helheten.

Det nya uppdraget ligger mellan dessa ytterligheter.

Den centrala utvecklingsfunktionen behöver vara starkare på riktning, lärande, samordning och kvalitetssäkring, men svagare på detaljkontroll. Den behöver skapa förutsättningar för att utvecklingsområdena kan ta ansvar, utan att släppa ansvaret för att helheten hänger ihop.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva den centrala utvecklingsfunktionens uppdrag i en decentraliserad arkitekturorganisation,
- skilja mellan styrning genom kontroll och styrning genom riktning,
- identifiera vilka arkitekturfrågor som bör drivas centralt och vilka som bör ägas nära utvecklingsområdena,
- formulera konkreta arbetssätt för stöd, samordning och kvalitetssäkring utan att skapa onödiga flaskhalsar.

## Innan vi börjar

I kapitel 1 introducerades enterprise arkitektur som en gemensam organisatorisk förmåga. I kapitel 2 introducerades kontinuerlig utvecklingslogik och arkitekturellt lärande.

Det här kapitlet bygger vidare på båda dessa idéer. Om arkitektur är en gemensam förmåga behöver den centrala funktionen inte göra allt själv. Om utveckling sker kontinuerligt behöver den centrala funktionen inte vänta på stora beslutspunkter för att bidra.

Tre nya huvudbegrepp används i kapitlet:

- **Riktningsskapande**: att formulera, förankra och vidareutveckla den gemensamma riktning som lokala beslut behöver förhålla sig till.
- **Aktiverande stöd**: stöd som gör utvecklingsområdena mer kapabla att själva ta ansvar, i stället för att skapa beroende av central expertis.
- **Helhetskvalitet**: kvaliteten i hur organisationens samlade utveckling hänger ihop över tid, inte bara kvaliteten i enskilda lösningar.

## Huvudförklaring

### Det centrala uppdraget förändras, men försvinner inte

När arkitekturarbetet decentraliseras kan det låta som att den centrala utvecklingsfunktionen blir mindre viktig. I praktiken är det ofta tvärtom.

Ju mer ansvar som flyttas ut i utvecklingsområdena, desto viktigare blir det att någon hjälper organisationen att se mönster, beroenden, gemensamma behov och långsiktiga konsekvenser. Utan en sådan funktion kan varje område fatta rimliga beslut var för sig, men ändå skapa en svårhanterlig helhet.

Den centrala funktionen behöver därför flytta sin tyngdpunkt.

I en mer traditionell faslogik kan den centrala funktionen ofta arbeta genom att granska underlag, delta vid beslutspunkter och säkerställa att projekt följer etablerade riktlinjer. I en mer agil och decentraliserad utvecklingslogik behöver funktionen i stället arbeta tidigare, oftare och mer dialogbaserat.

Det innebär inte att all granskning ska försvinna. Vissa beslut är fortfarande så viktiga, dyra eller svåra att ändra att de behöver tydlig kvalitetssäkring. Men granskning kan inte vara huvudformen för samverkan. Om arkitekturarbete främst märks när någon säger nej, kommer utvecklingsområdena att uppfatta arkitektur som ett hinder.

Den centrala funktionen behöver i stället vara känd för att hjälpa organisationen att fatta bättre beslut.

### Från kontrollinstans till riktningsskapare

En kontrollinstans frågar ofta: följer detta våra regler?

En riktningsskapare frågar också: leder detta oss åt rätt håll, och vad behöver vi lära oss för att kunna justera riktningen?

Skillnaden är viktig. Regler och principer kan skapa tydlighet, men de kan inte täcka alla situationer. I en decentraliserad organisation uppstår många lokala vägval där svaret inte finns färdigt. Då behöver utvecklingsområdena förstå den större riktningen, inte bara känna till en lista med krav.

Riktningsskapande handlar därför om att göra helheten begriplig och användbar. Det kan ske genom målarkitektur, principer, gemensamma vägval, prioriterade förmågor, standarder, referensmodeller och tydliga arkitekturella ambitioner. Men det viktigaste är inte dokumenten i sig. Det viktigaste är att de används i verkliga beslut.

En central utvecklingsfunktion som arbetar riktningsskapande behöver därför ställa frågor som:

- Vilka gemensamma förmågor är viktigast att stärka de kommande åren?
- Vilka arkitekturella risker ser vi återkommande i flera utvecklingsområden?
- Var behöver organisationen vara strikt, och var kan områdena ha större frihet?
- Vilka beslut behöver fattas en gång för helheten, och vilka bör fattas lokalt?
- Vilka mönster i lokala lösningar visar att vår gemensamma riktning behöver förtydligas?

Detta är en annan typ av arbete än att bara granska färdiga lösningar. Det kräver närvaro, dialog och förmåga att översätta mellan strategiska mål och vardagliga utvecklingsbeslut.

### Aktiverande stöd gör områdena starkare

Det är lätt att stöd blir en form av dold centralisering.

Om varje utvecklingsområde måste fråga den centrala funktionen för att förstå principer, tolka målarkitektur eller bedöma beroenden, har organisationen inte blivit särskilt decentraliserad. Den har bara flyttat besluten till en mer informell kö.

Aktiverande stöd har ett annat mål. Det ska öka utvecklingsområdenas egen förmåga att göra bra arkitekturella avvägningar.

Det kan handla om att den centrala funktionen:

- erbjuder enkla metoder för arkitekturanalys,
- hjälper områdena att formulera egna målarkitekturer som passar helheten,
- tillhandahåller mallar för arkitekturbeslut,
- faciliterar tvärområdesdialoger när beroenden är otydliga,
- coachar områdesarkitekter och utvecklingsledare,
- samlar lärdomar från flera områden och gör dem återanvändbara.

Skillnaden mot traditionellt expertstöd är att målet inte är att den centrala funktionen ska lösa frågan åt området. Målet är att området ska bli bättre på att lösa liknande frågor nästa gång.

Ett enkelt test är att fråga: efter vårt stöd, blev mottagaren mer självständig eller mer beroende av oss?

### Kvalitetssäkring behöver ske både före, under och efter

I en faslogik kopplas kvalitetssäkring ofta till beslutspunkter. Ett initiativ passerar en grind, ett underlag granskas och ett beslut fattas. Det kan fortfarande vara relevant i vissa situationer, men det räcker inte i en agil utvecklingslogik.

När utveckling sker löpande behöver kvalitetssäkring också ske löpande.

Det kan göras på tre sätt.

För det första kan kvalitetssäkring ske **före** arbete startar, genom tydliga ramar, principer och tidig dialog om arkitekturella konsekvenser.

För det andra kan kvalitetssäkring ske **under** arbetets gång, genom regelbundna avstämningar, forum, gemensamma beslut och stöd i svåra avvägningar.

För det tredje kan kvalitetssäkring ske **efter** viktiga vägval, genom lärande uppföljning. Vad blev konsekvensen? Stämde våra antaganden? Behöver principer eller riktning justeras?

Den sista delen är ofta underutvecklad. Organisationer är vanligtvis bättre på att besluta än på att lära av besluten. Men i en agil arkitekturorganisation är lärandet en del av kvaliteten.

### Den centrala funktionen ska se tvärs över områden

Utvecklingsområdena har nära kontakt med de verksamhetsdelar de stödjer. Det är en styrka. De ser behov, detaljer, lokala hinder och konkreta prioriteringar.

Men just därför kan de också få svårt att se mönster som uppstår tvärs över organisationen.

Den centrala utvecklingsfunktionen behöver ha ett annat perspektiv. Den ska inte ersätta områdenas lokala kunskap, men den ska kunna upptäcka frågor som är större än ett område:

- flera områden bygger liknande lösningar,
- flera områden har beroenden till samma informationsobjekt,
- flera områden tolkar samma princip på olika sätt,
- flera områden påverkas av samma tekniska skuld,
- flera områden behöver samma gemensamma förmåga,
- flera lokala prioriteringar drar helheten åt olika håll.

När sådana mönster syns behöver den centrala funktionen kunna ta initiativ. Inte nödvändigtvis genom att skapa ett stort program, utan genom att samla rätt personer, formulera frågan, synliggöra konsekvenser och föreslå nästa steg.

Det är här funktionen blir en viktig motor för helheten.

## Exempel

Tänk dig att tre utvecklingsområden samtidigt börjar arbeta med olika delar av kund- eller ärendeinformation.

Om varje område arbetar isolerat kan besluten verka rimliga. Ett område behöver förbättra handläggning. Ett annat behöver stärka digital självservice. Ett tredje behöver skapa bättre uppföljning. Alla har legitima behov och alla vill röra sig snabbt.

Efter några månader upptäcker organisationen att områdena har skapat olika begrepp, olika integrationsmönster och olika tolkningar av vilken information som är gemensam. Inget område har gjort något uppenbart fel, men helheten har blivit svagare.

I en kontrollorienterad modell skulle den centrala funktionen kanske granska lösningarna sent och begära omtag. Det skapar frustration och fördröjning.

I en aktiverande och riktningsskapande modell agerar den centrala funktionen tidigare. Den ser att flera områden rör sig mot samma informationsdomän, samlar områdesarkitekter och verksamhetsrepresentanter, tydliggör vilka begrepp som behöver vara gemensamma och vilka som kan vara lokala, och hjälper områdena att formulera gemensamma arkitekturbeslut.

Den centrala funktionen äger inte varje lösningsdetalj. Men den tar ansvar för att helheten inte tappas bort.

## Vanliga misstag

- **Misstag: Den centrala funktionen försöker godkänna för mycket.**
  - Varför det händer: Det finns en oro för spretighet och kvalitetsbrister.
  - Hur man undviker det: Skilj på beslut som kräver central kvalitetssäkring och beslut som kan fattas lokalt inom tydliga ramar.

- **Misstag: Stöd blir beroendeskapande.**
  - Varför det händer: Utvecklingsområdena vänjer sig vid att central expertis löser svåra frågor.
  - Hur man undviker det: Ge metoder, mallar, coachning och återkoppling som stärker områdets egen förmåga.

- **Misstag: Den centrala funktionen blir för strategisk och för långt från vardagen.**
  - Varför det händer: Helhetsperspektivet kopplas främst till planer, modeller och styrdokument.
  - Hur man undviker det: Delta i verkliga vägval och använd lokala beslut som test av om den gemensamma riktningen fungerar.

- **Misstag: Decentralisering tolkas som att varje område får göra som det vill.**
  - Varför det händer: Organisationen vill undvika tung centralstyrning.
  - Hur man undviker det: Kombinera lokal frihet med gemensamma principer, tydliga guardrails och forum för tvärgående frågor.

## Övningar

### Övning 1: Sortera den centrala funktionens arbete

Lista de arkitekturaktiviteter som den centrala utvecklingsfunktionen gör i dag. Sortera dem i fyra grupper:

1. Riktningsskapande
2. Aktiverande stöd
3. Kvalitetssäkring
4. Administration eller otydligt värde

Diskutera sedan:

- Vilken grupp tar mest tid?
- Vilken grupp skapar mest värde för helheten?
- Vilka aktiviteter borde minska?
- Vilka aktiviteter borde stärkas?

### Övning 2: Hitta rätt nivå för beslut

Välj tre aktuella arkitekturfrågor i organisationen. För varje fråga, bedöm om den bör:

- beslutas centralt,
- beslutas av ett utvecklingsområde,
- beslutas gemensamt av flera områden,
- hanteras som ett experiment med senare uppföljning.

Motivera varje val.

### Fördjupning: Formulera ett uppdrag

Skriv ett kort uppdragsutkast för den centrala utvecklingsfunktionen med fyra rubriker:

- Vi skapar riktning genom att ...
- Vi stödjer utvecklingsområden genom att ...
- Vi kvalitetssäkrar helheten genom att ...
- Vi undviker att bli flaskhals genom att ...

Jämför utkastet med hur funktionen arbetar i dag.

## Snabb sammanfattning

- Den centrala utvecklingsfunktionen blir inte oviktig i en decentraliserad organisation; den får ett annat uppdrag.
- Huvuduppgiften är att skapa riktning, stödja områdena och kvalitetssäkra helheten utan att detaljstyra allt.
- Stöd bör vara aktiverande: det ska göra utvecklingsområdena mer självständiga och arkitekturellt mogna.
- Kvalitetssäkring behöver ske före, under och efter utvecklingsarbete, inte bara vid formella beslutspunkter.
- Den centrala funktionen behöver se mönster tvärs över områden och ta initiativ när helheten kräver det.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan att vara kontrollinstans och att vara riktningsskapare?
2. Hur kan stöd från den centrala funktionen bli beroendeskapande?
3. Vilka typer av arkitekturfrågor bör normalt inte ägas av ett enskilt utvecklingsområde?
4. Hur kan kvalitetssäkring ske under pågående utveckling?
5. Vilka tecken visar att den centrala funktionen har blivit en flaskhals?

## Nästa steg

I nästa kapitel flyttas perspektivet från den centrala utvecklingsfunktionen till utvecklingsområdena. Om den centrala funktionen ska arbeta mer riktningsskapande och stödjande behöver varje utvecklingsområde också ta ett tydligare ansvar för sin del av arkitekturen. Kapitel 4 handlar därför om utvecklingsområdets arkitekturansvar.
