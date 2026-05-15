# Kapitel 9: Gemensamma förmågor, plattformar och standarder

## Varför detta kapitel finns

I en decentraliserad arkitekturorganisation finns en ständig spänning mellan lokal handlingskraft och gemensam nytta. Utvecklingsområdena behöver kunna agera snabbt utifrån sina verksamhetsbehov. Samtidigt finns frågor där lokala lösningar, om de får växa helt oberoende av varandra, skapar onödig komplexitet för hela organisationen.

Det är här gemensamma förmågor, plattformar och standarder blir viktiga.

De kan göra organisationen snabbare, säkrare och mer sammanhållen. De kan minska dubblering, förenkla integration, skapa bättre informationskvalitet och göra det lättare för utvecklingsområden att bygga vidare på varandras arbete. Men de kan också bli ett hinder om de införs som central detaljstyrning, som tvingande lösningar utan förankring eller som plattformar som inte svarar mot verkliga behov.

Detta kapitel handlar om hur organisationen kan avgöra när något bör vara gemensamt, hur gemensamma lösningar kan växa fram agilt och hur standarder kan användas som stöd utan att kväva utvecklingsområdenas ansvar.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- skilja mellan gemensam förmåga, gemensam plattform och standard
- resonera om när en fråga bör hanteras gemensamt och när lokal variation är rimlig
- beskriva hur gemensamma lösningar kan etableras utan att återgå till tung central styrning
- identifiera vanliga fallgropar vid införande av plattformar och standarder
- använda en enkel beslutsmodell för att bedöma graden av gemensamhet

## Innan vi börjar

I tidigare kapitel har vi talat om gemensam riktning, arkitekturforum, behovsflöden och beroenden. Dessa delar möts i frågan om gemensamma lösningar.

När ett beroende återkommer ofta kan det vara ett tecken på att organisationen behöver något gemensamt. När flera utvecklingsområden löser samma problem på olika sätt kan det vara ett tecken på dubblering. När varje område tolkar samma begrepp, krav eller tekniska mönster olika kan det vara ett tecken på att en standard saknas.

Men slutsatsen är inte automatiskt att allt ska centraliseras. I en agil decentraliserad organisation behöver gemensamhet motiveras av tydlig nytta, inte av vana.

## Huvudförklaring

### Tre olika saker som ofta blandas ihop

Orden gemensam förmåga, plattform och standard används ibland som om de betydde samma sak. Det gör samtalet otydligt. I denna bok skiljer vi på dem.

En **gemensam förmåga** är något organisationen behöver kunna göra på ett sammanhållet sätt. Det kan handla om identitetshantering, informationsutbyte, ärendehantering, analys, säkerhetsgranskning eller arkitekturellt beslutsstöd. Förmågan kan bestå av processer, kompetens, arbetssätt, information, teknik och ansvar.

En **gemensam plattform** är en teknisk eller organisatorisk grund som flera utvecklingsområden kan bygga på. En plattform kan vara ett system, en integrationsmiljö, en dataplattform, ett utvecklarstöd, en uppsättning tjänster eller ett återanvändbart ramverk.

En **standard** är en överenskommelse om hur något ska beskrivas, utformas, integreras, dokumenteras eller följas upp. Standarder kan gälla begrepp, gränssnitt, säkerhetsnivåer, dokumentationsformat, arkitekturbeslut, informationsmodeller eller tekniska mönster.

Skillnaden spelar roll:

- En gemensam förmåga svarar på frågan: *vad behöver organisationen kunna göra gemensamt?*
- En gemensam plattform svarar på frågan: *vilken grund kan flera bygga på?*
- En standard svarar på frågan: *vilka regler eller överenskommelser ska skapa konsekvens?*

Om organisationen blandar ihop dessa riskerar den att köpa eller bygga en plattform när problemet egentligen är otydligt ansvar, eller skriva en standard när problemet egentligen är att en gemensam förmåga saknas.

### Gemensamt är inte alltid bättre

Det kan låta självklart att gemensamma lösningar är effektivare än flera lokala lösningar. Ibland är det sant. Men inte alltid.

En gemensam lösning är ofta klok när:

- flera utvecklingsområden har samma eller mycket liknande behov
- säkerhet, spårbarhet eller regelefterlevnad kräver konsekvens
- informationsutbyte kräver gemensamma begrepp och gränssnitt
- lokal variation skapar hög kostnad eller risk för helheten
- återanvändning ger tydlig nytta utan att bromsa viktig utveckling
- kompetens och drift blir orimligt splittrad om alla väljer själva

Lokal variation är ofta rimlig när:

- behoven skiljer sig mycket mellan verksamhetsdelar
- lösningen behöver utforskas innan organisationen vet vad som bör standardiseras
- kostnaden för gemensamhet är större än nyttan
- en lokal lösning inte skapar betydande beroenden
- utvecklingsområdet själv kan bära konsekvenserna av sitt val

Gemensamhet ska därför inte vara ett reflexsvar. Den ska vara ett medvetet arkitekturbeslut.

### Från central produkt till gemensam tjänst

I en XLPM-präglad miljö kan gemensamma lösningar ofta växa fram som stora centrala projekt. Organisationen identifierar ett behov, formulerar krav, beslutar om projekt, bygger lösningen och förväntar sig därefter att utvecklingsområdena ska använda den.

Det kan fungera när behovet är stabilt och väl förstått. Men i en mer agil organisation är risken att den gemensamma lösningen blir för sen, för stor eller för långt från användarnas verkliga behov.

Ett mer agilt sätt är att behandla gemensamma lösningar som tjänster till utvecklingsområdena. Då behöver den centrala utvecklingsfunktionen inte bara fråga: “Vilken standard ska gälla?” utan också:

- Vilka problem försöker utvecklingsområdena lösa?
- Vilken minsta gemensamma lösning skulle ge nytta snabbt?
- Vilka områden är redo att pröva lösningen först?
- Hur fångar vi lärande från användning?
- När ska lösningen vara frivillig, rekommenderad eller bindande?

En gemensam plattform som ingen vill använda är inte en framgång, även om den är tekniskt korrekt. En gemensam standard som inte hjälper vardagens beslut kommer att kringgås. Därför behöver gemensamma lösningar utvecklas med samma lyhördhet som andra produkter.

### Tre mognadssteg för gemensamhet

Ett praktiskt sätt att undvika för tidig centralisering är att se gemensamhet i tre mognadssteg.

#### 1. Utforska

I det utforskande steget finns flera lokala varianter eller experiment. Organisationen vet ännu inte vad som bör bli gemensamt. Den centrala utvecklingsfunktionen följer utvecklingen, samlar lärdomar och hjälper områdena att se likheter och skillnader.

Frågan är: *Vad lär vi oss av att flera prövar olika lösningar?*

#### 2. Samordna

I samordningssteget börjar mönster bli tydliga. Några lösningar fungerar bättre än andra. Flera områden har liknande behov. Beroenden eller kostnader börjar bli synliga. Då kan organisationen skapa rekommendationer, referensarkitektur, gemensamma begrepp eller frivilliga tjänster.

Frågan är: *Vilken gemensam riktning ger nytta utan att låsa för tidigt?*

#### 3. Standardisera

I standardiseringssteget är nyttan med gemensamhet tydlig och kostnaden för variation hög. Då kan organisationen besluta om bindande riktning, obligatoriska gränssnitt, gemensam plattform eller tydliga avvecklingsplaner för avvikande lösningar.

Frågan är: *Vilken gemensamhet behöver vara bindande för att skydda helheten?*

Dessa steg hjälper organisationen att skilja mellan sådant som behöver växa fram och sådant som faktiskt behöver styras.

### Den centrala utvecklingsfunktionens roll

Den centrala utvecklingsfunktionen har en viktig roll, men inte som ensam beställare av allt gemensamt. Rollen är snarare att skapa förutsättningar för klok gemensamhet.

Det kan innebära att funktionen:

- identifierar återkommande behov och beroenden mellan områden
- tar initiativ till gemensamma förmågor där helheten kräver det
- hjälper områden att jämföra lokala lösningar och dela lärande
- formulerar principer, referensarkitektur och standarder
- kvalitetssäkrar att gemensamma lösningar inte blir onödigt tunga
- följer upp om gemensamma plattformar faktiskt skapar nytta
- stödjer avveckling av lösningar som skapar hög komplexitet

Det är viktigt att den centrala funktionen inte bara säger nej till lokal variation. Den behöver också kunna säga ja till gemensam investering när flera områden annars tvingas lösa samma problem var för sig.

### Utvecklingsområdets roll

Utvecklingsområdena har också ansvar för gemensamhet. De kan inte enbart se gemensamma lösningar som något som kommer “uppifrån”. Eftersom de sitter närmast behoven är deras erfarenheter avgörande.

Ett utvecklingsområde behöver därför:

- synliggöra när lokala behov återkommer i flera områden
- beskriva konsekvenser av lokala vägval för helheten
- bidra med erfarenheter från lösningar som fungerar
- pröva gemensamma tjänster och ge konkret återkoppling
- motivera avsteg från standarder när lokal variation behövs
- ta ansvar för avveckling när lokala lösningar ersätts av gemensamma

I en decentraliserad arkitekturorganisation är gemensamhet något som skapas mellan nivåer, inte något som bara beslutas centralt.

### En enkel beslutsmodell: gemensamhetsmatrisen

När organisationen diskuterar om något bör vara gemensamt kan följande frågor användas:

| Fråga | Låg gemensamhetsgrad | Hög gemensamhetsgrad |
|---|---|---|
| Hur många områden har behovet? | Ett eller få områden | Många områden |
| Hur lika är behoven? | Varierande och osäkra | Likartade och återkommande |
| Hur stor är risken med variation? | Begränsad lokal påverkan | Stor påverkan på säkerhet, information, kostnad eller helhet |
| Hur mogen är lösningsbilden? | Osäker, behöver utforskas | Väl prövad och stabil |
| Hur stor är kostnaden för samordning? | Hög i förhållande till nyttan | Rimlig i förhållande till nyttan |
| Hur viktigt är tempo lokalt? | Högt och unikt | Kan stödjas av gemensam lösning |

Om flera svar pekar mot höger är det troligt att organisationen bör samordna eller standardisera. Om flera svar pekar mot vänster är det ofta bättre att tillåta lokal variation, åtminstone under en period.

## Exempel

I den återkommande organisationen arbetar tre utvecklingsområden med olika delar av verksamheten. Alla behöver hantera externa parter och behörigheter, men de har historiskt byggt egna lösningar.

Område A har en enkel lösning som fungerar för deras ärenden. Område B har en mer avancerad lösning med många specialfall. Område C planerar att bygga nytt eftersom deras nuvarande lösning är svår att förvalta.

Tidigare hade detta kanske blivit ett centralt projekt med ambitionen att ersätta allt på en gång. Nu väljer den centrala utvecklingsfunktionen ett annat arbetssätt.

Först kartläggs behoven tillsammans med områdena. Det visar sig att vissa delar är gemensamma: identitet, behörighetsnivåer, loggning och grundläggande spårbarhet. Andra delar skiljer sig: verksamhetsregler, handläggningsflöden och undantag.

Organisationen beslutar därför att:

- skapa en gemensam förmåga för identitet och behörighet
- etablera en plattformstjänst för de delar som är lika
- ta fram en standard för begrepp och spårbarhet
- låta områdena behålla lokal variation i verksamhetsregler
- införa lösningen stegvis med ett område som första användare

Det viktiga är inte att allt blir gemensamt direkt. Det viktiga är att organisationen skiljer mellan det som bör vara gemensamt och det som bör vara lokalt.

## Vanliga misstag

### Misstag: Att standardisera för tidigt

**Varför det händer:** Organisationen vill snabbt skapa ordning och minska variation. Det kan kännas tryggt att besluta om en standard innan behoven är tillräckligt förstådda.

**Hur man undviker det:** Använd utforskande riktning när kunskapen är osäker. Låt standarder växa fram ur prövade mönster, inte bara ur önskan om kontroll.

### Misstag: Att kalla allt plattform

**Varför det händer:** Plattform låter konkret och handlingsinriktat. Då kan organisationen börja bygga teknik innan den har förstått vilken förmåga som faktiskt behövs.

**Hur man undviker det:** Börja med förmågan. Fråga vad organisationen behöver kunna göra, vilka ansvar som krävs och först därefter vilken teknisk grund som behövs.

### Misstag: Att göra gemensamma lösningar obligatoriska utan användarnytta

**Varför det händer:** Den centrala funktionen vill säkra helheten och minska variation. Men om lösningen inte hjälper utvecklingsområdena i deras vardag kommer den att upplevas som hinder.

**Hur man undviker det:** Behandla gemensamma lösningar som tjänster. Mät användning, nytta, ledtid, stödbehov och upplevd kvalitet.

### Misstag: Att tillåta lokal variation utan ansvar

**Varför det händer:** Organisationen vill vara agil och undvika central styrning. Det kan leda till att områden väljer fritt utan att redovisa konsekvenser.

**Hur man undviker det:** Tillåt avsteg, men kräv motivering, konsekvensbedömning och plan för uppföljning. Lokal frihet behöver kopplas till lokalt ansvar.

## Övningar

### Övning 1: Bedöm en gemensamhetsfråga

Välj en fråga i din organisation där flera utvecklingsområden har liknande behov. Det kan vara en plattform, standard, informationsmodell, integrationslösning eller gemensam arbetsprocess.

Besvara frågorna:

1. Är detta främst en gemensam förmåga, en plattform eller en standard?
2. Hur många områden berörs?
3. Hur lika är behoven?
4. Vilken risk skapar lokal variation?
5. Är lösningen mogen nog att standardiseras?
6. Bör organisationen utforska, samordna eller standardisera?

### Övning 2: Identifiera onödig och nödvändig variation

Gör en lista över tre områden där organisationen har olika lokala lösningar. För varje område, markera om variationen är:

- nödvändig för verksamheten
- acceptabel under en övergångsperiod
- onödig och kostnadsdrivande
- riskfylld för helheten

Diskutera vad som krävs för att gå från lokal variation till gemensam riktning.

### Fördjupning

Välj en befintlig gemensam plattform eller standard. Intervjua två utvecklingsområden om hur den upplevs.

Fråga:

- Vilket problem hjälper den er att lösa?
- Var skapar den friktion?
- Vilka lokala behov stödjer den inte?
- Vilken förändring skulle göra den mer användbar?
- Är den rätt nivå av bindande, vägledande eller utforskande?

Sammanfatta svaren som underlag till arkitekturforumet.

## Snabb sammanfattning

- Gemensamma förmågor, plattformar och standarder är olika saker och behöver diskuteras som olika saker.
- Gemensamhet är värdefull när den minskar risk, dubblering och komplexitet eller skapar tydlig nytta för flera områden.
- Lokal variation är rimlig när behoven skiljer sig, lösningen är osäker eller konsekvenserna är lokalt hanterbara.
- Gemensamma lösningar bör utvecklas agilt och behandlas som tjänster till utvecklingsområdena.
- Den centrala utvecklingsfunktionen ska hjälpa organisationen att hitta rätt nivå av gemensamhet, inte automatiskt centralisera allt.
- Utvecklingsområdena behöver bidra med behov, erfarenheter och ansvar för konsekvenser.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan en gemensam förmåga, en gemensam plattform och en standard?
2. När kan lokal variation vara bättre än en gemensam lösning?
3. Vilka risker uppstår om organisationen standardiserar för tidigt?
4. Hur kan en central utvecklingsfunktion stödja gemensamhet utan att detaljstyra?
5. Vilka tecken visar att ett återkommande lokalt behov bör lyftas till gemensam nivå?

## Nästa steg

När organisationen börjar skapa gemensamma förmågor, plattformar och standarder ökar behovet av ett fungerande gemensamt minne. Beslut, motiveringar, avsteg och lärdomar behöver kunna återanvändas över tid. Nästa kapitel handlar därför om arkitekturdokumentation som gemensamt minne: hur dokumentation kan göras lättviktig, användbar och levande i en agil decentraliserad organisation.
