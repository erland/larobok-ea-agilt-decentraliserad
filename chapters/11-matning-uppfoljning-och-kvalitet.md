# Kapitel 11: Mätning, uppföljning och kvalitet i arkitekturarbetet

## Varför detta kapitel finns

När en organisation går från XLPM-präglad fasstyrning till mer agila arbetssätt uppstår ofta en oro: hur vet vi att arkitekturarbetet håller tillräcklig kvalitet när färre beslut tas i stora centrala grindar?

Frågan är rimlig, men svaret kan inte vara att återinföra samma tunga kontroll som organisationen försöker lämna. I en decentraliserad arkitekturorganisation behöver kvalitet följas upp på ett sätt som stärker lärande, transparens och ansvar nära arbetet. Uppföljningen ska hjälpa organisationen att upptäcka mönster, risker och förbättringsbehov, inte bara kontrollera om enskilda dokument finns på rätt plats.

Detta kapitel handlar om hur mätning och uppföljning kan användas för att utveckla arkitekturförmågan. Fokus ligger på praktiska kvalitetsindikatorer, gemensamma uppföljningsrytmer och hur den centrala utvecklingsfunktionen kan stödja helheten utan att ta över det lokala ansvaret.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara skillnaden mellan kontrollmått och lärandemått i arkitekturarbetet
- beskriva vad arkitekturell kvalitet kan betyda i en decentraliserad organisation
- välja ett litet antal indikatorer som visar om arkitekturarbetet fungerar
- utforma uppföljning som stärker både lokal ansvarsförmåga och gemensam riktning
- identifiera vanliga fallgropar när arkitektur mäts och följs upp

## Innan vi börjar

Tidigare kapitel har beskrivit hur riktning, forum, behovsflöden, beroenden, gemensamma förmågor och dokumentation kan fungera i en decentraliserad arkitekturorganisation. Alla dessa delar behöver följas upp.

Om organisationen har arkitekturprinciper behöver den veta om principerna faktiskt används. Om det finns arkitekturforum behöver organisationen veta om forumen hjälper beslut eller skapar väntan. Om utvecklingsområdena ansvarar för lokalt arkitekturarbete behöver organisationen se om de har förutsättningar att ta det ansvaret. Om dokumentation ska vara ett gemensamt minne behöver någon märka när minnet blir inaktuellt.

Uppföljning är därför inte ett separat styrningslager. Den är en del av det löpande lärandet.

## Huvudförklaring

### Från kontrollpunkt till återkopplingssystem

I ett mer fasorienterat arbetssätt är uppföljning ofta kopplad till beslutspunkter. Har projektet tagit fram rätt underlag? Är granskningen genomförd? Är beslutet dokumenterat? Kan projektet gå vidare?

Den typen av kontroll kan fortfarande behövas i vissa sammanhang, särskilt vid stora investeringar, hög risk eller reglerade krav. Men den räcker inte i en agil och decentraliserad organisation. Där sker många arkitekturella vägval löpande, ofta innan de syns som formella beslut.

Organisationen behöver därför tänka på uppföljning som ett återkopplingssystem. Ett återkopplingssystem hjälper organisationen att se om arbetssätten ger önskad effekt och om riktningen behöver justeras.

Frågan blir inte bara:

> Har vi följt processen?

Frågan blir också:

> Blir våra arkitekturbeslut bättre, snabbare och mer sammanhängande över tid?

Det är en annan sorts uppföljning. Den kräver färre men bättre signaler.

### Arkitekturell kvalitet som mer än teknisk kvalitet

I den här boken används begreppet arkitekturell kvalitet för att beskriva hur väl organisationens arkitekturarbete stödjer långsiktig verksamhetsnytta, sammanhang och förändringsförmåga.

Det handlar alltså inte bara om teknisk kvalitet i system. Det handlar också om:

- om lokala initiativ stödjer gemensam riktning
- om beroenden upptäcks i tid
- om beslut fattas på rätt nivå
- om gemensamma förmågor används när de bör användas
- om avsteg är synliga och motiverade
- om dokumentation hjälper andra att förstå och agera
- om arkitekturforum skapar framdrift snarare än kö

Arkitekturell kvalitet kan därför inte mätas med ett enda tal. Den behöver förstås genom flera kompletterande signaler.

### Kontrollmått och lärandemått

Ett kontrollmått visar om något har gjorts. Exempel:

- antal genomförda arkitekturgranskningar
- andel initiativ med dokumenterad konsekvensbedömning
- antal beslut i beslutsloggen
- antal avsteg från en standard

Kontrollmått kan vara användbara, men de kan också skapa fel beteenden. Om organisationen bara mäter om dokument finns kan människor börja producera dokument utan att dokumenten används. Om organisationen bara mäter antal forumärenden kan forumet bli en rapporteringskanal snarare än en beslutsyta.

Ett lärandemått visar om arbetssättet hjälper organisationen att bli bättre. Exempel:

- hur ofta beroenden upptäcks innan de blir akuta problem
- om återkommande avsteg visar att en princip behöver förtydligas
- om utvecklingsområden upplever att de får bättre stöd över tid
- om beslut kan fattas närmare arbetet utan att helhetskvaliteten försämras
- om dokumentation återanvänds i nya initiativ

Lärandemått kräver ofta mer dialog än kontrollmått. De är ibland kvalitativa. Det gör dem inte svagare. I komplexa organisationer är kvalitet ofta något man behöver förstå genom mönster, samtal och konsekvenser, inte bara genom siffror.

### Tre nivåer av uppföljning

En decentraliserad arkitekturorganisation behöver uppföljning på flera nivåer.

#### 1. Lokal uppföljning i utvecklingsområdet

Utvecklingsområdet följer upp sin egen områdesarkitektur, sina lokala vägval, sina beroenden och sin användning av gemensam riktning.

Exempel på frågor:

- Vilka viktiga arkitekturbeslut har vi fattat den senaste perioden?
- Vilka beroenden har förändrats?
- Vilka avsteg har vi gjort, och varför?
- Vilka delar av vår områdesarkitektur är osäkra eller inaktuella?
- Vilka kommande behov kräver arkitekturell konsekvensbedömning?

Syftet är inte att rapportera allt centralt. Syftet är att området ska kunna äga sin arkitektur med bättre medvetenhet.

#### 2. Gemensam uppföljning mellan områden

När flera utvecklingsområden påverkar varandra behövs gemensam uppföljning. Den kan ske i arkitekturforum, portföljdialoger eller särskilda samverkansmöten.

Exempel på frågor:

- Vilka beroenden kräver gemensam prioritering?
- Vilka standarder eller gemensamma förmågor skapar friktion?
- Vilka beslut behöver eskaleras eftersom påverkan är bred?
- Var ser vi samma problem uppstå i flera områden?
- Vilka principer behöver förtydligas?

Syftet är att se mönster över gränserna. Här blir den centrala utvecklingsfunktionen viktig som samordnare och mönsterupptäckare.

#### 3. Strategisk uppföljning av helhetskvalitet

På strategisk nivå behöver organisationen följa om arkitekturförmågan stödjer verksamhetens långsiktiga utveckling.

Exempel på frågor:

- Rör sig utvecklingen i linje med gemensam målarkitektur?
- Har organisationen rätt balans mellan lokal autonomi och gemensamma vägval?
- Finns teknisk eller verksamhetsmässig skuld som växer över områdesgränser?
- Behöver centrala initiativ startas för att hantera återkommande hinder?
- Finns tillräcklig beslutskapacitet i utvecklingsområdena?

Denna uppföljning bör inte bli en tung årsövning. Den behöver ske i en återkommande rytm där slutsatser påverkar prioriteringar, riktning och stöd.

### Vad den centrala utvecklingsfunktionen bör följa upp

Den centrala utvecklingsfunktionen ska inte försöka mäta allt. Då riskerar den att bli en administrativ kontrollfunktion. Den bör i stället följa upp sådant som visar om helheten håller ihop.

Ett praktiskt startpaket kan vara fem indikatorområden:

| Indikatorområde | Vad det visar | Exempel på uppföljningsfråga |
|---|---|---|
| Riktning | Om gemensamma principer och målarkitektur används | Vilka återkommande avsteg ser vi, och vad säger de om riktningen? |
| Beroenden | Om områden upptäcker och hanterar påverkan i tid | Vilka beroenden blev sena, dyra eller otydliga? |
| Beslut | Om beslut fattas på rätt nivå och med tillräcklig kvalitet | Vilka beslut fastnade, och varför? |
| Lärande | Om erfarenheter från initiativ påverkar kommande vägval | Vilka lärdomar har återanvänts i andra områden? |
| Förmåga | Om utvecklingsområdena kan ta sitt arkitekturansvar | Var behövs stöd, kompetens eller gemensamma arbetssätt? |

Detta är inte en rapportmall som måste fyllas i varje månad. Det är en struktur för dialog. Den hjälper den centrala funktionen att se när den bör ta initiativ, när den bör stödja och när den bör låta områdena agera själva.

### Kvalitetsdialog före kvalitetsrapport

I många organisationer finns en tendens att göra uppföljning till rapportering. Någon frågar efter status. Någon annan fyller i status. Informationen skickas vidare. I bästa fall används den. I sämsta fall blir den ett parallellt administrativt flöde.

För arkitekturarbete är dialog ofta viktigare än rapport. En kvalitetsdialog är ett återkommande samtal där centrala och lokala aktörer tillsammans tolkar signaler.

En bra kvalitetsdialog kan handla om:

- vilka mönster som syns i beslutsloggen
- vilka avsteg som är rimliga och vilka som tyder på problem
- vilka beroenden som behöver mer aktiv hantering
- vilka principer som är svåra att tillämpa
- var utvecklingsområden behöver stöd för att ta ansvar

Dialogen bör vara konkret. Den ska utgå från verkliga initiativ, beslut och konsekvenser. Då blir uppföljningen ett sätt att förbättra arkitekturarbetet, inte bara beskriva det.

### När mätning blir styrning

Det som mäts påverkar beteende. Om organisationen mäter antal granskningar kan den få fler granskningar. Om den mäter antal godkända dokument kan den få fler dokument. Om den mäter avvikelser utan att skilja mellan klok lokal anpassning och riskfyllda avsteg kan den skapa rädsla för transparens.

Därför måste varje mått granskas utifrån vilken styrsignal det skickar.

En enkel kontrollfråga är:

> Om människor optimerar för detta mått, blir arkitekturarbetet bättre eller bara mer rapporterbart?

Om svaret är “mer rapporterbart” bör måttet ändras, kompletteras eller tas bort.

### Uppföljningsrytm

Uppföljning behöver en rytm. Utan rytm blir den reaktiv. Med för tung rytm blir den administrativ. En möjlig modell är:

- **Varje iteration eller månad:** lokala områdesdialoger om aktuella vägval, beroenden och beslut.
- **Varje månad eller kvartal:** gemensam arkitekturdialog mellan utvecklingsområden och central utvecklingsfunktion.
- **Varje kvartal eller tertial:** helhetsgenomgång av riktning, återkommande avsteg, beroendemönster och behov av centrala initiativ.
- **Årligen eller vid större förändringar:** omprövning av målarkitektur, principer, forumstruktur och styrmodell.

Exakta intervall är mindre viktiga än att rytmen är användbar. Uppföljningen ska komma tillräckligt ofta för att påverka arbetet, men inte så ofta att den stjäl kraft från arbetet.

## Exempel

Organisationen i vårt återkommande scenario märker att flera utvecklingsområden gör avsteg från en gemensam integrationsprincip. I det gamla arbetssättet hade detta kunnat hanteras som bristande efterlevnad: områdena följer inte principen och behöver korrigeras.

Den centrala utvecklingsfunktionen väljer i stället att använda avstegen som lärandesignal.

I kvalitetsdialogen visar det sig att tre olika saker ligger bakom avstegen:

1. Ett område har ett verkligt undantagsfall där principen skulle bli orimligt dyr.
2. Ett annat område har missförstått när principen gäller.
3. Ett tredje område upplever att den gemensamma plattformen inte har tillräcklig kapacitet för deras behov.

Samma mätpunkt, “antal avsteg”, visar alltså tre olika typer av förbättringsbehov.

Den centrala utvecklingsfunktionen gör därför tre olika saker:

- dokumenterar det första avsteget som ett accepterat undantag med villkor
- förtydligar principen och skapar ett kort exempel
- startar en dialog om plattformens kapacitet som möjlig gemensam förbättring

Uppföljningen blir därmed inte kontroll för kontrollens skull. Den blir ett sätt att förbättra riktning, stöd och gemensam förmåga.

## Vanliga misstag

- **Misstag: Att mäta det som är lättast att räkna.**  
  - Varför det händer: Antal dokument, möten och granskningar är enkla att samla in.  
  - Hur man undviker det: Komplettera enkla mått med frågor om effekt, lärande och beslutskvalitet.

- **Misstag: Att använda uppföljning för att återcentralisera ansvar.**  
  - Varför det händer: Central funktion vill säkra helheten och börjar begära mer detaljerad rapportering.  
  - Hur man undviker det: Följ upp helhetsmönster, men låt utvecklingsområdena äga sina lokala åtgärder.

- **Misstag: Att tolka alla avsteg som problem.**  
  - Varför det händer: Avsteg ses som bristande efterlevnad.  
  - Hur man undviker det: Skilj mellan riskfyllda avsteg, motiverade undantag och signaler om att riktningen behöver justeras.

- **Misstag: Att skapa rapportering utan återkoppling.**  
  - Varför det händer: Uppföljningen byggs för styrkedjan, inte för dem som gör arbetet.  
  - Hur man undviker det: Säkerställ att varje uppföljning leder till dialog, beslut, stöd eller förbättring.

- **Misstag: Att mäta arkitektur som om den vore statisk.**  
  - Varför det händer: Målarkitektur och principer behandlas som färdiga produkter.  
  - Hur man undviker det: Följ upp om riktningen fortfarande hjälper organisationen att fatta bra beslut.

## Övningar

### Övning 1: Välj fem kvalitetsindikatorer

Välj ett utvecklingsområde eller en central arkitekturförmåga. Formulera fem indikatorer som tillsammans visar om arkitekturarbetet fungerar.

För varje indikator, skriv:

- vad indikatorn ska visa
- vem som använder informationen
- hur ofta den bör följas upp
- vilken dialog eller åtgärd den kan leda till
- vilket oönskat beteende indikatorn kan skapa om den används fel

### Övning 2: Gör om ett kontrollmått till ett lärandemått

Välj ett befintligt eller tänkt kontrollmått, till exempel “antal genomförda arkitekturgranskningar”.

Besvara:

1. Vad säger måttet faktiskt?
2. Vad säger det inte?
3. Vilket beteende kan det skapa?
4. Hur kan det kompletteras med ett lärandemått?
5. Vilken fråga bör diskuteras i en kvalitetsdialog?

### Fördjupning: Skapa en uppföljningsrytm

Skissa en uppföljningsrytm för en decentraliserad arkitekturorganisation.

Beskriv:

- vad som följs upp lokalt i utvecklingsområdena
- vad som följs upp gemensamt mellan områden
- vad den centrala utvecklingsfunktionen följer upp på helhetsnivå
- vilka forum som används
- hur resultatet leder till förbättring, inte bara rapportering

## Snabb sammanfattning

- I agila och decentraliserade organisationer behöver uppföljning fungera som återkopplingssystem, inte bara kontrollpunkt.
- Arkitekturell kvalitet handlar om hur väl utvecklingen hänger ihop, stödjer verksamheten och möjliggör förändring över tid.
- Kontrollmått visar om något har gjorts; lärandemått visar om arbetssättet hjälper organisationen att bli bättre.
- Uppföljning bör ske lokalt, gemensamt mellan områden och strategiskt på helhetsnivå.
- Den centrala utvecklingsfunktionen bör följa mönster, beroenden, beslut, lärande och förmåga.
- Kvalitetsdialoger är ofta viktigare än kvalitetsrapporter.
- Mått måste väljas med omsorg eftersom de påverkar beteende.

## Quiz/reflektionsfrågor

1. Varför räcker det inte att mäta antal arkitekturgranskningar?
2. Vad är skillnaden mellan ett kontrollmått och ett lärandemått?
3. Ge två exempel på signaler som kan visa att en arkitekturprincip behöver förtydligas.
4. Vilka delar av arkitekturell kvalitet bör följas upp lokalt i ett utvecklingsområde?
5. Hur kan den centrala utvecklingsfunktionen följa upp helheten utan att ta över det lokala ansvaret?
6. Vilka risker uppstår om alla avsteg behandlas som problem?
7. Vad bör en kvalitetsdialog leda till för att vara meningsfull?

## Nästa steg

I nästa kapitel knyter vi ihop bokens delar och beskriver hur organisationen kan bygga en hållbar decentraliserad arkitekturförmåga över tid. Då handlar det inte bara om enskilda arbetssätt, utan om kultur, ansvar, lärande och långsiktig förändringskraft.
