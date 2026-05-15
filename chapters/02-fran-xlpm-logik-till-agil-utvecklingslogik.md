# Kapitel 2: Från XLPM-logik till agil utvecklingslogik på organisationsnivå

## Varför detta kapitel finns

I föregående kapitel beskrev vi varför enterprise arkitektur inte längre kan förstås som något som ägs centralt och levereras till resten av organisationen. När utvecklingsområdena får större ansvar för att fånga behov, prioritera och driva förändring behöver arkitekturarbetet också ske närmare där besluten uppstår.

Detta kapitel fördjupar själva förändringen i arbetssätt.

Många organisationer som rör sig mot agila arbetssätt bär fortfarande med sig vanor från projekt- och fasstyrning. XLPM används här som en förenklad referens till ett sådant sätt att tänka: tydliga faser, beslutspunkter, omfattande förberedelser och en stark idé om att rätt underlag ska tas fram innan genomförandet startar.

Det arbetssättet har styrkor. Det kan skapa ordning, ansvar och spårbarhet. Men när organisationen går mot mer kontinuerlig utveckling förändras förutsättningarna. Behov, lösningar och prioriteringar blir inte färdiga vid en beslutspunkt. De växer fram stegvis.

För enterprise arkitektur innebär det att arbetet behöver flytta från att främst kvalitetssäkra före genomförande till att också stödja löpande lärande, löpande vägval och löpande samordning.

## Lärandemål

Efter kapitlet ska läsaren kunna:

- beskriva skillnaden mellan XLPM-präglad faslogik och agil utvecklingslogik,
- förklara varför arkitektur behöver bli mer kontinuerlig i en agil organisation,
- identifiera vilka arkitekturella risker som uppstår när gamla styrvanor lever kvar i nya agila strukturer,
- föreslå hur enterprise arkitektur kan stödja både riktning och lärande över tid.

## Innan vi börjar

Det här kapitlet använder tre huvudbegrepp:

- **Faslogik**: ett sätt att organisera utveckling där arbete delas upp i tydliga steg, ofta med beslutspunkter mellan stegen.
- **Kontinuerlig utvecklingslogik**: ett sätt att organisera utveckling där behov, lösningar, prioriteringar och lärande hanteras löpande.
- **Arkitekturellt lärande**: den kunskap som organisationen bygger upp när den prövar lösningar, upptäcker konsekvenser och justerar riktningen.

Begreppen används inte för att säga att det ena alltid är rätt och det andra alltid är fel. Poängen är att visa att olika logiker kräver olika sätt att arbeta med enterprise arkitektur.

## Huvudförklaring

### Faslogiken bygger på förberedelse

I en XLPM-präglad miljö finns ofta en tydlig idé om att utvecklingsarbete ska förberedas noggrant. Innan ett projekt går vidare behöver mål, omfattning, lösningsförslag, kostnader, risker och beroenden beskrivas.

För enterprise arkitektur har detta ofta passat väl. Arkitekter har kunnat analysera verksamhetens behov, beskriva målbild, granska lösningsalternativ och lämna rekommendationer inför beslut.

Det kan skapa värde, särskilt när förändringen är stor, dyr, riskfylld eller svår att ändra i efterhand.

Men faslogiken har också en inbyggd svaghet: den antar ofta att mycket går att veta tidigt.

I komplexa förändringar stämmer det sällan fullt ut. Verksamhetens behov förtydligas när användare möter lösningen. Tekniska begränsningar upptäcks när teamen börjar bygga. Beroenden mellan områden blir tydliga först när flera initiativ pågår samtidigt. Juridiska, informationsmässiga eller organisatoriska konsekvenser kan visa sig senare än planerat.

När arkitektur hanteras som en tidig fas riskerar därför viktiga arkitekturbeslut att antingen bli för teoretiska eller komma för sent.

### Agil utvecklingslogik bygger på lärande

I en mer agil utvecklingslogik är utgångspunkten en annan. Organisationen accepterar att den inte vet allt från början. Den arbetar i kortare cykler, prioriterar om när ny kunskap uppstår och försöker skapa nytta stegvis.

Det betyder inte att planering försvinner. Det betyder att planering blir mer levande.

För arkitekturarbetet innebär detta ett skifte:

| I faslogik | I agil utvecklingslogik |
|---|---|
| Arkitektur tas ofta fram före genomförande. | Arkitektur utvecklas och förfinas löpande. |
| Kvalitetssäkring sker vid beslutspunkter. | Kvalitetssäkring sker genom återkommande dialog och vägval. |
| Avvikelser ses ofta som problem mot plan. | Ny kunskap ses som underlag för justering. |
| Central granskning kan vara huvudmekanism. | Gemensamma ramar, forum och lärande blir viktigare. |
| Dokumentation används för att beskriva beslut innan arbete startar. | Dokumentation används för att bevara viktiga vägval och gemensam förståelse. |

Det viktiga är inte att byta ord. Det viktiga är att ändra rytm.

Om organisationen säger att den arbetar agilt men fortfarande förväntar sig att arkitekturen ska vara färdig, godkänd och stabil innan utveckling startar, uppstår en konflikt. Teamen och utvecklingsområdena arbetar då i en lärande logik, medan styrningen försöker hålla fast vid en förutsägande logik.

### Arkitektur måste finnas före, under och efter

En vanlig missuppfattning är att agil utveckling innebär att arkitektur ska skjutas upp tills behovet blir tydligt. Det är lika problematiskt som att försöka bestämma allt i början.

I en decentraliserad organisation behöver arkitektur finnas i tre tidsperspektiv samtidigt.

**Före arbetet** behövs gemensam riktning. Organisationen behöver veta vilka principer, mål och ramar som gäller. Utvecklingsområdena behöver förstå vilka frågor som är lokala och vilka som påverkar helheten.

**Under arbetet** behövs stöd för vägval. När team och områden möter konkreta problem behöver arkitekturkompetens finnas nära nog för att bidra i tid. Det kan handla om informationsmodeller, integrationer, återanvändning, säkerhet, plattformar eller beroenden.

**Efter arbetet** behövs lärande. Beslut behöver följas upp. Antaganden behöver testas. Det som visade sig fungera bör spridas. Det som skapade skuld eller komplexitet behöver hanteras.

Enterprise arkitektur blir då inte en station i processen. Den blir ett sätt att hålla ihop riktning, beslut och lärande över tid.

### När gamla vanor följer med in i nya arbetssätt

Många organisationer förändrar sin struktur snabbare än sina vanor.

Man inför utvecklingsområden, agila team, backloggar och nya planeringsforum. Samtidigt finns gamla förväntningar kvar:

- att stora beslut ska vara färdigutredda innan arbete startar,
- att avvikelser från plan är något negativt,
- att centrala forum främst ska godkänna,
- att arkitekturdokumentation ska vara komplett innan utveckling får påbörjas,
- att ansvar kan säkras genom process snarare än genom aktiv dialog.

Det skapar ofta dubbelstyrning. Utvecklingsområdena förväntas ta ansvar och röra sig snabbt, men bromsas av styrformer som bygger på att ansvar ska kontrolleras centralt.

Samtidigt kan den centrala utvecklingsfunktionen känna motsatt problem: när beslut fattas lokalt och snabbt uppstår oro för att helheten tappas bort.

Båda reaktionerna är begripliga. Därför behöver organisationen inte bara införa agila ceremonier eller nya roller. Den behöver omförhandla hur arkitekturellt ansvar fungerar.

### Från beslutspunkt till beslutskapacitet

Ett användbart sätt att beskriva skiftet är att gå från fokus på beslutspunkter till fokus på beslutskapacitet.

En beslutspunkt svarar på frågan: “Får vi gå vidare?”

Beslutskapacitet svarar på frågan: “Har vi förmågan att fatta tillräckligt bra beslut löpande?”

För enterprise arkitektur är detta avgörande. I en decentraliserad organisation kommer många beslut aldrig att passera ett centralt forum. Det vore varken möjligt eller önskvärt. Därför behöver organisationen bygga förmåga där besluten faktiskt uppstår.

Det kan göras genom:

- tydliga arkitekturprinciper,
- lättillgängligt stöd från den centrala utvecklingsfunktionen,
- gemensamma arbetssätt för att beskriva arkitekturella vägval,
- återkommande forum för lärande och samordning,
- tydliga kriterier för när en fråga ska lyftas,
- transparens kring beroenden och konsekvenser.

Målet är inte att eliminera formella beslut. Vissa beslut behöver fortfarande fattas tydligt och spårbart. Målet är att formella beslut inte ska vara den enda mekanismen för arkitekturell kvalitet.

## Exempel

Ett utvecklingsområde får i uppdrag att förbättra en digital tjänst för en viss verksamhetsprocess. I en tidigare XLPM-präglad modell hade arbetet kanske inletts med ett projektförslag, en förstudie, en lösningsarkitektur och en beslutspunkt innan genomförande.

I den nya organisationen arbetar utvecklingsområdet i stället med en backlogg. Behov prioriteras löpande tillsammans med verksamheten. Teamen börjar med att förbättra ett avgränsat flöde och lär sig mer efter hand.

Efter några iterationer upptäcker området att tjänsten behöver hämta information från ett annat utvecklingsområde. Man inser också att informationen definieras olika i de två områdena. Den lokala förbättringen har alltså blivit en arkitekturfråga för helheten.

I en gammal logik kan detta uppfattas som ett problem: “Detta borde ha utretts tidigare.”

I en agil utvecklingslogik är det snarare ett normalt uttryck för lärande. Frågan är inte vem som borde ha vetat allt från början. Frågan är hur organisationen snabbt kan hantera den nya kunskapen.

Ett fungerande arkitekturarbete skulle då kunna se ut så här:

1. Utvecklingsområdet beskriver vägvalet och konsekvensen kort.
2. Den centrala utvecklingsfunktionen hjälper till att se om frågan berör fler områden.
3. Berörda områden samlas för att komma överens om gemensam informationsdefinition eller integrationsprincip.
4. Beslutet dokumenteras lättviktigt så att nästa område inte behöver börja om.
5. Lärdomen förs tillbaka till gemensamma principer eller vägledning om det finns ett återkommande mönster.

Det viktiga är att arkitekturen inte stoppar lärandet. Den hjälper organisationen att ta hand om lärandet.

## Vanliga misstag

### Misstag: Att tro att agil utveckling gör tidig arkitektur onödig

Varför det händer: Organisationen vill bort från tunga förstudier och långsam fasstyrning.

Hur man undviker det: Skilj mellan att bestämma allt i förväg och att ge tillräcklig riktning i förväg. Agilt arbete behöver arkitektur, men arkitekturen behöver vara levande.

### Misstag: Att behålla gamla beslutspunkter men byta namn på dem

Varför det händer: Organisationen vill modernisera arbetssättet men är fortfarande beroende av gamla kontrollmekanismer.

Hur man undviker det: Granska varje forum och beslutspunkt. Fråga om den skapar bättre beslut, snabbare lärande och tydligare ansvar — eller bara återskapar gammal faslogik.

### Misstag: Att låta varje utvecklingsområde tolka agilitet på egen hand

Varför det händer: Decentralisering uppfattas som att varje område ska hitta sitt eget arbetssätt.

Hur man undviker det: Skapa gemensamma minimiramar för arkitekturella vägval, beroenden, dokumentation och eskalering. Låt detaljerna vara lokala, men håll ihop de frågor som påverkar helheten.

### Misstag: Att dokumentera för mycket för tidigt och för lite efteråt

Varför det händer: I faslogik dokumenteras mycket inför beslut. I agil utveckling finns risk att dokumentation ses som hinder.

Hur man undviker det: Dokumentera mindre före, men bättre över tid. Fånga viktiga beslut, antaganden, konsekvenser och lärdomar när de faktiskt uppstår.

## Övningar

### Övning 1: Identifiera kvarvarande faslogik

Välj ett aktuellt utvecklingsflöde i organisationen.

Svara på frågorna:

- Var förväntas arkitektur vara “klar” innan arbetet får fortsätta?
- Vilka beslutspunkter finns kvar från tidigare arbetssätt?
- Vilka av dem skapar verklig kvalitet?
- Vilka skapar främst väntan, dubbelarbete eller otydlighet?
- Var uppstår ny arkitekturell kunskap under arbetets gång?

Avsluta med att markera en beslutspunkt som bör behållas, en som bör förändras och en som bör ersättas med löpande dialog.

### Övning 2: Bygg en enkel modell för kontinuerlig arkitektur

Skissa ett arbetssätt för ett utvecklingsområde där arkitektur finns med före, under och efter arbetet.

Använd tre rubriker:

1. **Före**: Vilken gemensam riktning behöver området känna till?
2. **Under**: När och hur får området arkitekturstöd?
3. **Efter**: Hur fångas lärdomar och beslut så att helheten stärks?

Diskutera vilka delar som bör vara gemensamma för alla utvecklingsområden och vilka delar som kan vara lokala.

### Fördjupning

Välj ett arkitekturbeslut som nyligen fattats i organisationen.

Analysera beslutet utifrån två perspektiv:

- Hur hade beslutet hanterats i en XLPM-präglad faslogik?
- Hur borde beslutet hanteras i en agil utvecklingslogik?

Jämför skillnaden i ansvar, timing, dokumentation, forum och uppföljning.

## Snabb sammanfattning

- XLPM-präglad faslogik bygger ofta på tidig förberedelse, beslutspunkter och kontroll före genomförande.
- Agil utvecklingslogik bygger mer på löpande prioritering, stegvis lärande och kontinuerliga vägval.
- Enterprise arkitektur behöver därför fungera före, under och efter utvecklingsarbetet.
- Den centrala utvecklingsfunktionen behöver hjälpa organisationen att bygga beslutskapacitet, inte bara kontrollera beslutspunkter.
- Utvecklingsområden behöver kunna fatta lokala beslut inom gemensamma ramar och lyfta frågor när de påverkar helheten.
- Dokumentation behöver bli lättare, mer levande och mer inriktad på viktiga beslut och lärdomar.

## Quiz/reflektionsfrågor

1. Vilka delar av er nuvarande styrning bygger fortfarande på faslogik?
2. Var uppstår arkitekturell kunskap först efter att utvecklingsarbete har startat?
3. Vilka arkitekturbeslut behöver fortfarande formella beslutspunkter?
4. Vilka beslut bör i stället stödjas genom principer, forum och löpande dialog?
5. Hur kan den centrala utvecklingsfunktionen hjälpa utvecklingsområdena att fatta bättre beslut utan att bli en flaskhals?

## Nästa steg

I nästa kapitel går vi vidare till den centrala utvecklingsfunktionens nya uppdrag. Vi tittar på hur funktionen kan ta initiativ till viktiga helhetsfrågor, stödja utvecklingsområden och kvalitetssäkra gemensam riktning utan att återgå till central detaljkontroll.
