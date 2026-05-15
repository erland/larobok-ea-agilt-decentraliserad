# Kapitel 5: Gemensam riktning utan detaljstyrning

## Varför detta kapitel finns

I föregående kapitel beskrev vi utvecklingsområdets arkitekturansvar. Ett utvecklingsområde behöver kunna förstå sin del av helheten, fånga behov, bedöma arkitekturella konsekvenser och fatta beslut nära verksamheten.

Men lokalt ansvar räcker inte i sig.

Om varje utvecklingsområde tolkar sitt uppdrag isolerat kan organisationen snabbt få flera olika riktningar samtidigt. Lösningar kan börja överlappa. Informationsflöden kan bli svåra att hålla ihop. Plattformar kan växa isär. Beslut som är rimliga lokalt kan skapa kostnader och begränsningar för andra delar av organisationen.

Därför behövs gemensam riktning.

Den svåra frågan är hur riktningen ska skapas utan att organisationen går tillbaka till tung detaljstyrning. I en mer agil organisation behöver riktningen vara tillräckligt tydlig för att hjälpa lokala beslut, men tillräckligt levande för att kunna justeras när organisationen lär sig.

Det här kapitlet handlar om den balansen.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- förklara skillnaden mellan gemensam riktning och central detaljstyrning,
- beskriva hur principer, målarkitektur och guardrails kan användas i ett decentraliserat arbetssätt,
- identifiera när riktning behöver vara bindande och när den bör vara vägledande,
- formulera enkla riktlinjer som hjälper utvecklingsområden att fatta beslut utan att vänta på central godkännande,
- se hur gemensam riktning behöver underhållas genom lärande och återkoppling.

## Innan vi börjar

I kapitel 3 beskrev vi den centrala utvecklingsfunktionens uppdrag att skapa riktning, ge stöd och kvalitetssäkra helheten. I kapitel 4 beskrev vi hur utvecklingsområdena behöver ta lokalt arkitekturägarskap.

Det här kapitlet binder ihop dessa två perspektiv.

Tre huvudbegrepp används i kapitlet:

- **Gemensam riktning**: en sammanhållen bild av vart organisationens utveckling ska röra sig och vilka avvägningar som ska vägleda beslut.
- **Arkitekturprincip**: en vägledande regel som hjälper organisationen att fatta konsekventa beslut.
- **Guardrail**: en tydlig ram som ger handlingsfrihet inom accepterade gränser.

## Huvudförklaring

### Riktning är inte samma sak som kontroll

När en organisation tidigare har arbetat med stark projekt- och fasstyrning kan riktning ofta förväxlas med kontroll. Det kan finnas en vana att riktning uttrycks genom planer, beslutspunkter, dokument, granskningar och godkännanden.

I ett sådant sammanhang blir enterprise arkitektur lätt något som håller ordning genom att säga ja eller nej.

I en decentraliserad och mer agil organisation behöver riktning fungera annorlunda. Den ska inte i första hand vara ett filter i slutet av en process. Den ska vara ett stöd tidigt, när utvecklingsområden formar behov, prioriterar och väljer väg.

Gemensam riktning svarar på frågor som:

- Vilka verksamhetsförmågor är strategiskt viktiga att stärka?
- Vilka informationsflöden behöver hänga ihop över områdesgränser?
- Vilka plattformar, tjänster eller standarder ska återanvändas?
- Vilka typer av lösningar vill organisationen undvika?
- Vilka kvaliteter är viktigast över tid, till exempel säkerhet, spårbarhet, flexibilitet eller kostnadskontroll?
- Vilka kompromisser är acceptabla lokalt, och vilka påverkar helheten för mycket?

Riktning handlar alltså inte om att den centrala funktionen ska bestämma varje lösning. Den handlar om att lokala beslut ska kunna dras åt samma håll.

### Detaljstyrning skapar ofta falsk trygghet

Detaljstyrning kan kännas trygg. Om alla beslut ska granskas centralt verkar risken minska. Om alla utvecklingsområden måste följa samma dokument verkar helheten bli säkrad.

Men i praktiken kan detaljstyrning skapa andra problem.

För det första kan den centrala funktionen bli en flaskhals. Beslut som borde fattas nära verksamheten väntar på granskning. Utvecklingsområdena lär sig att arkitektur är något som någon annan godkänner, inte något de själva ansvarar för.

För det andra kan detaljer snabbt bli inaktuella. I ett agilt arbetssätt förändras kunskapen löpande. Behov omformuleras, lösningsalternativ prövas och beroenden upptäcks. Om riktningen är för detaljerad behöver den ständigt skrivas om.

För det tredje kan detaljstyrning minska ansvarstagandet. Om ett utvecklingsområde bara följer en central instruktion kan det bli oklart vem som äger konsekvenserna när verkligheten inte passar instruktionen.

Det betyder inte att allt ska vara frivilligt. Vissa saker behöver vara tydliga och ibland bindande. Men bindningen bör ligga där helhetsrisken är stor, inte där den lokala variationen är ofarlig.

### En användbar riktning har flera nivåer

Gemensam riktning behöver kunna uttryckas på olika nivåer. Om allt formuleras som övergripande visioner blir det svårt att använda i vardagen. Om allt formuleras som detaljerade instruktioner blir det svårt att anpassa lokalt.

En praktisk modell är att skilja mellan fyra nivåer:

1. **Strategisk riktning**: vad organisationen vill uppnå över tid.
2. **Arkitekturprinciper**: vilka avvägningar som ska vägleda beslut.
3. **Målarkitektur eller målbild**: hur viktiga delar av helheten bör utvecklas.
4. **Guardrails**: vilka ramar som lokala lösningar behöver hålla sig inom.

Den strategiska riktningen kan till exempel säga att organisationen vill minska dubbelarbete mellan utvecklingsområden och skapa mer sammanhållen information om medborgare, kunder, ärenden eller produkter.

En arkitekturprincip kan då säga: “Information som används av flera områden ska ha tydligt ägarskap och definierade gränssnitt.”

En målbild kan visa vilka informationsdomäner, tjänster eller plattformar som bör användas för att nå dit.

En guardrail kan säga: “Nya integrationer mellan områden ska exponeras via godkända API:er eller händelser, inte genom direkt åtkomst till varandras databaser.”

Tillsammans blir detta mer användbart än enbart en vision och mindre låsande än en detaljerad lösningsspecifikation för alla områden.

### Principer måste hjälpa verkliga beslut

Många organisationer har arkitekturprinciper som få använder. De kan vara för många, för generella eller skrivna på ett sätt som inte hjälper när verkliga avvägningar behöver göras.

En princip som säger “vi ska återanvända innan vi bygger nytt” låter klok, men den räcker inte alltid. Vad händer om återanvändning innebär högre beroende, sämre användarupplevelse eller längre ledtid? När är det ändå rätt att bygga nytt?

En användbar arkitekturprincip behöver därför innehålla mer än en formulering. Den bör också beskriva:

- varför principen finns,
- när den är särskilt viktig,
- vilka beslut den ska påverka,
- vilka undantag som kan vara rimliga,
- vem som behöver involveras när principen frångås.

Exempel:

**Princip:** Gemensamma informationsobjekt ska ha tydligt ägarskap.  
**Varför:** Organisationen behöver kunna lita på gemensam information över områdesgränser.  
**Påverkar beslut om:** datamodeller, integrationer, masterdata, rapportering och ansvarsfördelning.  
**Rimliga undantag:** tillfälliga lokala kopior kan accepteras när de är tidsbegränsade och har tydlig avvecklingsplan.  
**När frågan ska lyftas:** om flera utvecklingsområden behöver ändra eller tolka samma information på olika sätt.

På det sättet blir principen ett beslutsstöd, inte bara en formulering i ett dokument.

### Guardrails ger frihet genom tydliga gränser

Ett vanligt missförstånd är att ramar minskar agilitet. I själva verket kan rätt ramar öka handlingsfriheten.

Om utvecklingsområdena vet vilka gränser som gäller behöver de inte fråga om allt. De kan fatta beslut snabbare, så länge besluten håller sig inom ramarna.

En bra guardrail är konkret nog för att vara användbar, men inte så detaljerad att den låser lösningen i onödan.

Exempel på guardrails kan vara:

- Säkerhetsklassad information får inte lagras i lösningar som saknar godkänd skyddsnivå.
- Nya externa gränssnitt ska dokumenteras i organisationens gemensamma katalog.
- Ett utvecklingsområde får välja lokal lösning, men om lösningen påverkar två eller fler andra områden ska beroendet synliggöras i gemensamt forum.
- Avsteg från gemensam plattform ska ha tydlig motivering, tidsgräns och ägare.
- Nya datakällor som används för styrning eller uppföljning ska ha definierat informationsägarskap.

Guardrails bör inte vara en lång lista med regler som ingen minns. De bör vara få, tydliga och kopplade till de risker organisationen verkligen behöver hantera.

### Bindande, vägledande och utforskande riktning

All riktning behöver inte ha samma styrka. Ett vanligt problem är att organisationer antingen gör riktningen för lös eller för hård. Antingen blir allt rekommendationer, vilket gör det svårt att säkra helheten. Eller så blir allt krav, vilket gör arbetet långsamt och stelt.

Ett mer nyanserat arbetssätt är att skilja mellan tre typer av riktning:

| Typ av riktning | När den passar | Exempel |
|---|---|---|
| Bindande | När fel beslut kan skapa stor risk, hög kostnad eller svår återställning | säkerhetskrav, juridiska krav, gemensamma informationsprinciper |
| Vägledande | När konsekvens är viktig men lokal variation kan accepteras | rekommenderade integrationsmönster, namngivning, dokumentationsnivå |
| Utforskande | När organisationen behöver lära sig innan riktningen låses | nya tekniska mönster, nya arbetssätt, preliminära målarkitekturer |

Den centrala utvecklingsfunktionen behöver vara tydlig med vilken typ av riktning som gäller. Ett utvecklingsområde ska inte behöva gissa om en princip är ett krav, en rekommendation eller en hypotes.

Detta är särskilt viktigt i en organisation som går från XLPM till agilt arbetssätt. I faslogik kan det finnas en vana att styrdokument uppfattas som fasta. I agil utvecklingslogik behöver organisationen kunna säga: “Det här är bindande”, “det här är vår bästa rekommendation just nu” och “det här behöver vi pröva och lära oss mer om.”

### Riktning behöver ägare och rytm

Gemensam riktning blir snabbt gammal om ingen äger den. Den blir också svår att använda om den bara uppdateras i stora omtag.

Därför behöver riktningen ha både ägare och rytm.

Ägare betyder inte att en person eller funktion ensam bestämmer. Det betyder att någon ansvarar för att riktningen hålls levande, samlas in, prioriteras, formuleras och kommuniceras.

Rytm betyder att riktningen återkommer i organisationens arbetssätt. Den kan till exempel ses över:

- inför större prioriteringsbeslut,
- efter återkommande arkitekturforum,
- när flera utvecklingsområden stöter på samma problem,
- när ett viktigt avsteg har gjorts,
- när ny kunskap från ett initiativ förändrar tidigare antaganden.

Den centrala utvecklingsfunktionen har ofta ett naturligt ansvar för att hålla ihop detta. Men utvecklingsområdena behöver bidra med erfarenheter, avsteg, behov och konsekvenser från vardagen. Annars blir riktningen central teori snarare än gemensam praktik.

### Riktning behöver vara lätt att hitta och lätt att använda

En riktning som är svår att hitta används sällan. En riktning som är svår att tolka leder till olika lokala tolkningar.

Därför behöver gemensam riktning presenteras på ett sätt som passar användningen.

Det kan till exempel finnas:

- en kort översikt över de viktigaste arkitekturprinciperna,
- en målbild för några centrala verksamhets- eller informationsområden,
- en lista över aktuella guardrails,
- exempel på bra tillämpning,
- beslutade avsteg och varför de accepterats,
- kontaktvägar för frågor som behöver lyftas.

Det viktigaste är inte formatet. Det viktigaste är att riktningen hjälper människor i beslutssituationer.

En utvecklingsledare ska kunna använda den när ett initiativ formas. En områdesarkitekt ska kunna använda den när konsekvenser bedöms. Den centrala utvecklingsfunktionen ska kunna använda den när helheten följs upp. Ledningen ska kunna använda den när prioriteringar ställs mot varandra.

## Exempel

Tänk dig att tre utvecklingsområden i organisationen var för sig börjar utveckla lösningar för att hantera samma typ av grundinformation. Varje område har goda skäl. Deras verksamhetsbehov är olika, deras tidplaner skiljer sig åt och de upplever att en gemensam lösning skulle ta för lång tid.

I en centraliserad modell hade enterprise arkitektur kanske stoppat initiativen och krävt en gemensam lösningsdesign innan något fick gå vidare.

I en helt decentraliserad modell hade varje område kanske fortsatt på egen hand, vilket senare hade skapat dubbla register, oklara informationsägare och kostsamma integrationer.

Med gemensam riktning utan detaljstyrning kan organisationen agera annorlunda.

Den centrala utvecklingsfunktionen pekar på en arkitekturprincip: gemensam grundinformation ska ha tydligt ägarskap och återanvändbara gränssnitt. Det finns också en guardrail: nya lösningar som skapar eller ändrar gemensam grundinformation måste synliggöra informationsägare och beroenden till andra områden.

Utvecklingsområdena får därför inte bara bygga tre separata lösningar utan dialog. Men de behöver inte heller vänta på en komplett central målarkitektur. I stället gör de en gemensam konsekvensbedömning. De identifierar vilken information som faktiskt är gemensam, vilka delar som är lokala variationer och vilka gränssnitt som behövs.

Resultatet blir att ett område tar ansvar för den gemensamma informationskärnan, medan de andra områdena får bygga lokala stöd ovanpå den. Den centrala utvecklingsfunktionen dokumenterar beslutet som ett exempel på tillämpad riktning och uppdaterar målbilden för informationsområdet.

Det viktiga är inte att allt blev centralt. Det viktiga är att lokala initiativ drogs mot en gemensam riktning innan de hann skapa onödiga strukturella problem.

## Vanliga misstag

- **Misstag: Att göra riktningen för abstrakt.**
  - Varför det händer: Organisationen vill undvika detaljstyrning och formulerar därför bara övergripande ambitioner.
  - Hur man undviker det: Komplettera visioner med principer, exempel och guardrails som hjälper verkliga beslut.

- **Misstag: Att göra alla riktlinjer bindande.**
  - Varför det händer: Man vill säkra helheten och minska risken för lokala avsteg.
  - Hur man undviker det: Skilj mellan bindande, vägledande och utforskande riktning.

- **Misstag: Att låta den centrala funktionen äga riktningen ensam.**
  - Varför det händer: Enterprise arkitektur ses fortfarande som något centralt.
  - Hur man undviker det: Låt utvecklingsområden bidra med erfarenheter, avsteg, behov och lärande.

- **Misstag: Att inte förklara varför en princip finns.**
  - Varför det händer: Principer skrivs som regler snarare än beslutsstöd.
  - Hur man undviker det: Beskriv syfte, tillämpning, undantag och när frågan ska lyftas.

- **Misstag: Att blanda ihop avsteg med misslyckanden.**
  - Varför det händer: Organisationen är van vid efterlevnad som främsta kvalitetsmått.
  - Hur man undviker det: Behandla motiverade avsteg som källa till lärande och möjlig signal om att riktningen behöver justeras.

## Övningar

### Övning 1: Granska en princip

Välj en arkitekturprincip som finns i din organisation, eller formulera en tänkt princip.

Besvara följande frågor:

1. Vilket problem ska principen hjälpa organisationen att hantera?
2. Vilka beslut ska principen påverka?
3. Är principen bindande, vägledande eller utforskande?
4. Vilka undantag kan vara rimliga?
5. När behöver ett utvecklingsområde lyfta frågan till gemensamt forum?

Skriv sedan om principen så att den blir mer användbar i en konkret beslutssituation.

### Övning 2: Formulera tre guardrails

Utgå från ett utvecklingsområde som ofta behöver fatta beslut snabbt.

Formulera tre guardrails som skulle ge området större handlingsfrihet utan att helheten äventyras.

För varje guardrail, skriv:

- vilken risk den hanterar,
- vilka beslut den påverkar,
- hur ett område vet om det håller sig inom ramen,
- vad som ska hända om området behöver göra avsteg.

### Fördjupning: Hitta balansen mellan frihet och helhet

Rita upp två kolumner.

I den vänstra kolumnen skriver du beslut som bör kunna fattas lokalt i ett utvecklingsområde. I den högra kolumnen skriver du beslut som behöver gemensam riktning eller gemensam prövning.

Diskutera sedan:

- Vad gör att ett beslut hör hemma lokalt?
- Vad gör att ett beslut behöver lyftas?
- Vilka beslut ligger i gråzonen?
- Vilka guardrails skulle minska behovet av eskalering?

## Snabb sammanfattning

- Gemensam riktning ska hjälpa lokala beslut att stödja helheten.
- Riktning är inte samma sak som central detaljstyrning.
- En användbar riktning kan bestå av strategisk riktning, arkitekturprinciper, målarkitektur och guardrails.
- Arkitekturprinciper behöver förklara varför de finns och hur de ska användas.
- Guardrails skapar handlingsfrihet genom tydliga gränser.
- All riktning bör inte vara lika hård; skilj mellan bindande, vägledande och utforskande riktning.
- Riktningen behöver ägare, rytm och återkoppling från utvecklingsområdena.

## Quiz/reflektionsfrågor

1. Vad är skillnaden mellan gemensam riktning och detaljstyrning?
2. Varför kan detaljstyrning minska utvecklingsområdenas ansvarstagande?
3. Vad kännetecknar en användbar arkitekturprincip?
4. Hur kan guardrails öka handlingsfriheten i en decentraliserad organisation?
5. När bör en riktning vara bindande, och när bör den vara vägledande?
6. Hur kan utvecklingsområden bidra till att den gemensamma riktningen hålls levande?

## Nästa steg

I nästa kapitel går vi vidare till arkitekturforum. Om gemensam riktning ska fungera i praktiken behöver organisationen ha forum där frågor kan lyftas, avvägningar göras och lärande spridas. Utmaningen är att sådana forum ska stödja beslut, inte bli en ny flaskhals.
