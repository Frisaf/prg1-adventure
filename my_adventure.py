adventure = [
    {
        "id": 1,
        "title": "Välj din karaktär",
        "text": "Du vaknar upp i ett mörkt rum. Minnet är suddigt, men en sak är klar: du är fast i ett gammalt slott. "
                "Men vem är du egentligen? Välj din karaktär.",
        "options": [
            {"text": "Den tappra krigaren", "next_id": 2},
            {"text": "Den kloka magikern", "next_id": 3},
            {"text": "Den smidiga tjuven", "next_id": 4},
        ],
    },
    {
        "id": 2,
        "title": "Den tappra krigaren",
        "text": "Du är en krigare, stark och orädd. Dina muskler minns striden, även om ditt sinne är suddigt. "
                "Du ser en rostig svärdsklinga ligga på golvet. Kanske kan den vara till nytta?",
        "options": [
            {"text": "Plocka upp svärdet och undersök rummet", "next_id": 5},
            {"text": "Lämna svärdet och leta efter en utgång", "next_id": 6},
        ],
    },
    {
        "id": 3,
        "title": "Den kloka magikern",
        "text": "Du är en magiker, skicklig i de mystiska konsterna. Ditt sinne känns skarpt trots förvirringen. "
                "I din hand håller du en bok med uråldriga formler. Kanske kan du använda magi för att ta dig härifrån?",
        "options": [
            {"text": "Läs en besvärjelse ur boken", "next_id": 7},
            {"text": "Leta efter en dörr och försöka ta dig ut", "next_id": 8},
        ],
    },
    {
        "id": 4,
        "title": "Den smidiga tjuven",
        "text": "Du är en tjuv, snabb och listig. Dina fingrar är vana vid att dyrka lås och smyga i skuggorna. "
                "I din ficka hittar du ett litet låsverktyg. Kanske kan det hjälpa dig att fly?",
        "options": [
            {"text": "Försök dyrka upp dörren", "next_id": 9},
            {"text": "Utforska rummet först", "next_id": 10},
        ],
    },
    {
        "id": 5,
        "title": "Krigaren och svärdet",
        "text": "Du plockar upp svärdet. Det är tungt, men du känner dig tryggare med det i handen. "
                "När du ser dig omkring upptäcker du en gammal dörr, men den är låst.",
        "options": [
            {"text": "Försök bryta upp dörren med svärdet", "next_id": 11},
            {"text": "Leta efter en annan väg ut", "next_id": 12},
        ],
        "loot": "Rusty Sword",
    },
    {
        "id": 6,
        "title": "Krigaren utan vapen",
        "text": "Du bestämmer dig för att lämna svärdet och leta efter en annan utgång. "
                "Rummet är kalt, men en gammal bokhylla döljer något bakom sig.",
        "options": [
            {"text": "Flytta bokhyllan och se vad som finns bakom", "next_id": 13},
            {"text": "Ignorera bokhyllan och sök vidare", "next_id": 14},
        ],
    },
    {
        "id": 7,
        "title": "Magikern och besvärjelsen",
        "text": "Du bläddrar genom din bok och hittar en besvärjelse för att öppna låsta dörrar. "
                "Men orden verkar komplexa, och du är osäker på om du kan kontrollera magin.",
        "options": [
            {"text": "Försök kasta besvärjelsen", "next_id": 15},
            {"text": "Leta efter en annan utväg", "next_id": 16},
        ],
    },
    {
        "id": 8,
        "title": "Magikern och dörren",
        "text": "Du ignorerar magiboken och undersöker rummet. En dammig spegel hänger på väggen, "
                "men när du tittar i den ser du något som inte borde vara där – en dörr som inte syns i verkligheten.",
        "options": [
            {"text": "Rör vid spegeln för att se vad som händer", "next_id": 17},
            {"text": "Sök vidare i rummet", "next_id": 18},
        ],
    },
    {
        "id": 9,
        "title": "Tjuven och låset",
        "text": "Du tar fram ditt låsverktyg och börjar dyrka upp dörren. Det klickar till och dörren glider upp. "
                "Men på andra sidan väntar en mörk korridor med svaga ljusglimtar i fjärran.",
        "options": [
            {"text": "Gå försiktigt genom korridoren", "next_id": 19},
            {"text": "Sök efter något användbart i rummet innan du går vidare", "next_id": 20},
        ],
    },
    {
        "id": 10,
        "title": "Tjuven och utforskningen",
        "text": "Du bestämmer dig för att undersöka rummet först. I en gammal byrå hittar du en märklig nyckel "
                "med konstiga symboler ingraverade.",
        "options": [
            {"text": "Använd nyckeln på dörren", "next_id": 21},
            {"text": "Behåll nyckeln och försök dyrka låset ändå", "next_id": 9},
        ],
    },
    
    # Pusselavsnittet
    {
        "id": 11,
        "title": "Krigaren och den förstärkta dörren",
        "text": "Du hugger svärdet mot dörren, men den är gjord av en metall du aldrig sett förut. "
                "Ovanför dörren finns en stenplatta med ett inskrivet pussel.",
        "options": [
            {"text": "Försök lösa pusslet", "next_id": 22},
            {"text": "Ge upp och leta vidare", "next_id": 12},
        ],
    },
    {
        "id": 15,
        "title": "Magikern och den olösta formeln",
        "text": "Besvärjelsen skapar ett sken, men den verkar ofullständig. "
                "Ovanför dörren ser du en text ristad i sten. Det verkar vara en gåta.",
        "options": [
            {"text": "Försök lösa gåtan", "next_id": 22},
            {"text": "Leta efter en annan lösning", "next_id": 16},
        ],
    },
    {
        "id": 12,
        "title": "Krigaren söker en annan väg",
        "text": "Du bestämmer dig för att lämna svärdet och söka efter en annan väg ut. "
                "När du undersöker rummet märker du att en av väggarna känns ihålig. "
                "Efter en snabb knackning hittar du en lös sten.",
        "options": [
            {"text": "Dra ut stenen och se vad som finns bakom", "next_id": 13},
            {"text": "Ignorera stenen och fortsätt leta", "next_id": 14},
        ],
    },
    {
        "id": 13,
        "title": "Den dolda passagen",
        "text": "Bakom stenen hittar du en liten spak. När du drar i den öppnas en smal gång. "
                "Den är mörk och trång, men det verkar vara en väg ut.",
        "options": [
            {"text": "Kryp in i den smala gången", "next_id": 26},
            {"text": "Leta vidare i rummet", "next_id": 14},
        ],
    },
    {
        "id": 14,
        "title": "En återvändsgränd",
        "text": "Du fortsätter leta i rummet men hittar inget mer av värde. "
                "Det verkar som att enda vägen ut är att gå tillbaka och välja något annat.",
        "options": [
            {"text": "Plocka upp svärdet och försöka igen", "next_id": 5},
            {"text": "Gå tillbaka och undersöka väggen igen", "next_id": 13},
        ],
    },
    {
        "id": 16,
        "title": "Magikern letar efter en annan väg",
        "text": "Du ignorerar magiboken och börjar undersöka rummet. "
                "Bakom en gammal bokhylla hittar du ett märke på väggen – en symbol som matchar något i din bok.",
        "options": [
            {"text": "Studera symbolen noggrant", "next_id": 17},
            {"text": "Leta vidare", "next_id": 18},
        ],
    },
    {
        "id": 17,
        "title": "Den magiska insikten",
        "text": "När du granskar symbolen i kombination med din bok inser du att den döljer en portal. "
                "Med ett par viskade ord från en av bokens besvärjelser börjar väggen skifta färg.",
        "options": [
            {"text": "Gå genom den magiska väggen", "next_id": 26},
            {"text": "Vänta och se vad som händer", "next_id": 18},
        ],
    },
    {
        "id": 18,
        "title": "En tom väg",
        "text": "Du letar vidare, men rummet verkar vara tomt på andra ledtrådar. "
                "Den enda vägen verkar vara genom symbolen du hittade.",
        "options": [
            {"text": "Gå tillbaka och studera symbolen", "next_id": 17},
        ],
    },
    {
        "id": 19,
        "title": "Tjuven i korridoren",
        "text": "Du smyger försiktigt genom korridoren. Skuggorna rör sig längs väggarna, "
                "men det verkar vara en optisk illusion från fladdrande ljus.\n\n"
                "Längre fram ser du flera dörrar – en med konstiga symboler, en i silver och en som ser ut att vara en illusion.",
        "options": [
            {"text": "Öppna dörren med symbolerna", "next_id": 30},
            {"text": "Öppna den silverfärgade dörren", "next_id": 31},
            {"text": "Sträck ut handen mot illusionen", "next_id": 32},
        ],
    },
    {
        "id": 20,
        "title": "Tjuven hittar ett föremål",
        "text": "Innan du lämnar rummet letar du igenom en gammal kista. Där hittar du en nyckel med mystiska symboler på.",
        "options": [
            {"text": "Ta nyckeln och gå genom dörren", "next_id": 21},
            {"text": "Lämna nyckeln och gå vidare", "next_id": 19},
        ],
    },
    {
        "id": 20,
        "title": "Tjuven och rummet",
        "text": "Du letar runt i rummet, men allt du hittar är en nyckel. Denna nyckel ser ut att ha passat i låset, men du har ju redan dyrkat upp det...",
        "options": [
            {"text": "Gå vidare", "next_id": 19}
        ]
    },
    {
        "id": 21,
        "title": "Tjuven och den mystiska nyckeln",
        "text": "Nyckeln passar perfekt i dörren, men istället för att öppnas, börjar en panel i väggen lysa upp. "
                "En gåta visas på ytan.",
        "options": [
            {"text": "Försök lösa gåtan", "next_id": 22},
            {"text": "Försök dyrka upp låset istället", "next_id": 9},
        ],
    },
    {
        "id": 22,
        "title": "Pusslet",
        "text": "Gåtan lyder: 'Jag har nycklar men inga lås. Jag kan öppna men inte stänga. Vad är jag?'",
        "options": [
            {"text": "Ett piano", "next_id": 23},
            {"text": "En dörr", "next_id": 24},
            {"text": "En kod", "next_id": 25},
        ],
    },
    {
        "id": 23,
        "title": "Rätt svar!",
        "text": "Du uttalar ordet 'piano' och dörren framför dig glider sakta upp. "
                "Du har lyckats låsa upp den första vägen ut ur slottet!",
        "options": [
            {"text": "Gå vidare genom den öppna dörren", "next_id": 26},
        ],
    },
    {
        "id": 24,
        "title": "Fel svar...",
        "text": "Inget händer. Du hör ett mekaniskt klick, som om något låstes ännu hårdare.",
        "options": [
            {"text": "Försök igen", "next_id": 22},
        ],
    },
    {
        "id": 25,
        "title": "Fel svar...",
        "text": "Väggen skakar till men ingenting öppnas. Det känns som att något är fel.",
        "options": [
            {"text": "Försök igen", "next_id": 22},
        ],
    },
    {
        "id": 26,
        "title": "Den mörka korridoren",
        "text": "Du kliver in i en lång, mörk korridor. Väggarna är täckta av dammiga målningar av personer "
                "som verkar stirra på dig. Längs korridoren finns flera dörrar, och längst bort ser du en stor öppen port "
                "som leder ut i friheten. Kall nattluft strömmar in. \n\n"
                "Men något känns fel...",
        "options": [
            {"text": "Gå direkt mot den öppna porten", "next_id": 27},
            {"text": "Undersök dörrarna längs korridoren", "next_id": 28},
            {"text": "Studera målningarna på väggarna", "next_id": 29},
        ],
    },
    {
        "id": 27,
        "title": "Den bedrägliga friheten",
        "text": "Du skyndar dig mot den öppna porten. Ju närmare du kommer, desto mer känns det som att luften själv "
                "drar dig framåt. Precis när du kliver över tröskeln känner du en stark kraft dra dig bakåt...\n\n"
                "Du slungas genom luften och landar hårt på golvet.\n\n"
                "När du ser upp inser du att du är tillbaka i start-rummet där du först vaknade.",
        "options": [
            {"text": "Försök igen", "next_id": 26},
            {"text": "Den här vägen fungerar inte. Undersök korridoren istället.", "next_id": 28},
        ],
    },
    {
        "id": 28,
        "title": "Dörrarna i korridoren",
        "text": "Du bestämmer dig för att undersöka dörrarna längs korridoren. De verkar alla vara unika – en av dem "
                "är täckt av märkliga symboler, en annan ser ut att vara gjord av rent silver, och en tredje verkar vara "
                "bara en illusion, som om den inte existerar på riktigt.",
        "options": [
            {"text": "Öppna dörren med symbolerna", "next_id": 30},
            {"text": "Öppna den silverfärgade dörren", "next_id": 31},
            {"text": "Sträck ut handen mot illusionen", "next_id": 32},
        ],
    },
    {
        "id": 29,
        "title": "De stirrande målningarna",
        "text": "Du granskar målningarna noggrannare. De föreställer personer i gammaldags kläder, men något är fel... "
                "Deras ögon verkar följa dig när du rör dig. En av tavlorna har en liten inskription:\n\n"
                "'Endast den som förstår illusionens sanning kan undkomma förbannelsen.'",
        "options": [
            {"text": "Fundera över inskriptionen och fortsätt undersöka korridoren", "next_id": 28},
            {"text": "Gå mot den öppna porten ändå", "next_id": 27},
        ],
    },
    {
        "id": 30,
        "title": "Dörren med symbolerna",
        "text": "Du trycker ner handtaget på dörren med de mystiska symbolerna. Den öppnas långsamt och avslöjar ett litet rum "
                "fyllt av stearinljus och en stor stenplatta med inristade symboler. På väggen finns en spegel.\n\n"
                "När du närmar dig spegeln ser du inte din egen spegelbild – utan korridoren bakom dig, där den öppna porten "
                "är stängd istället för öppen.",
        "options": [
            {"text": "Studera stenplattan närmare", "next_id": 33},
            {"text": "Gå tillbaka till korridoren", "next_id": 28},
        ],
    },
    {
        "id": 31,
        "title": "Den silverfärgade dörren",
        "text": "Den silverfärgade dörren gnisslar när du öppnar den. Inuti finns en gammal tron, och på den sitter "
                "en skuggig figur. Dess ögon lyser svagt i mörkret.\n\n"
                "'Du söker en väg ut', säger figuren. 'Men inte alla vägar är som de ser ut.'\n\n"
                "Vid figurens fötter ligger en liten bok.",
        "options": [
            {"text": "Plocka upp boken och läsa den", "next_id": 34},
            {"text": "Fråga figuren om en väg ut", "next_id": 35},
            {"text": "Lämna rummet och gå tillbaka", "next_id": 28},
        ],
    },
    {
        "id": 32,
        "title": "Illusionsdörren",
        "text": "Du sträcker ut handen mot dörren, men den känns inte verklig. När du försöker gå igenom den "
                "sugs du plötsligt in i ett mörker. Allt snurrar runt dig, och du vaknar plötsligt i korridoren igen, "
                "precis framför målningarna.\n\n"
                "Det verkar som att denna dörr inte leder någonstans – eller så är du inte redo att använda den än.",
        "options": [
            {"text": "Gå tillbaka och undersök de andra dörrarna", "next_id": 28},
            {"text": "Gå direkt mot den öppna porten", "next_id": 27},
        ],
    },
    {
        "id": 33,
        "title": "Stenplattan med symbolerna",
        "text": "Du granskar stenplattan. Symbolerna ser bekanta ut, och när du jämför dem med inskriptionen på "
                "målningen i korridoren inser du något:\n\n"
                "Det handlar om illusioner. Korridoren visar en falsk utgång, men verkligheten reflekteras i spegeln.\n\n"
                "Du måste hitta ett sätt att använda denna kunskap för att fly.",
        "options": [
            {"text": "Gå tillbaka till spegeln och interagera med den", "next_id": 36},
            {"text": "Försök trycka på några av symbolerna", "next_id": 37},
        ],
    },
    {
        "id": 34,
        "title": "Den lilla boken",
        "text": "Du plockar upp boken och börjar bläddra. Det är en dagbok skriven av någon som en gång var fångad i slottet.\n\n"
                "'Endast de som ser genom lögnen kan fly', står det på en av sidorna. "
                "'Den öppna porten är en fälla. Den verkliga vägen ut är dold i reflektionen.'",
        "options": [
            {"text": "Tacka figuren och lämna rummet", "next_id": 28},
            {"text": "Fråga figuren vad han menar med reflektionen", "next_id": 35},
        ],
    },
    {
        "id": 35,
        "title": "Den skuggiga figurens ord",
        "text": "Figuren lutar sig framåt. 'Om du litar på dina ögon, förlorar du. Lita på det som speglas, "
                "så finner du sanningen.'\n\n"
                "Hans röst ekar i ditt huvud medan han sakta försvinner i mörkret.",
        "options": [
            {"text": "Ta hans råd och gå tillbaka till spegeln", "next_id": 36},
            {"text": "Lämna rummet och tänka på vad han sa", "next_id": 28},
        ],
    },
    {
        "id": 36,
        "title": "Spegelns sanning",
        "text": "Du ställer dig framför spegeln och inser att du måste agera annorlunda. "
                "Om spegeln visar en stängd port där den öppna egentligen är... då måste den verkliga utgången finnas där "
                "porten verkar vara stängd i spegeln!",
        "options": [
            {"text": "Gå mot den stängda porten i spegelns reflektion", "next_id": 38},
            {"text": "Rör vid spegeln och se om den reagerar", "next_id": 39},
        ],
    },
    {
        "id": 37,
        "title": "Fel val vid stenplattan",
        "text": "Du trycker på några av symbolerna, men ingenting händer... förutom att rummet börjar skaka. "
                "Plötsligt slungas du bakåt och vaknar upp tillbaka i korridoren.",
        "options": [
            {"text": "Gå tillbaka och försök igen", "next_id": 33},
        ],
    },
    {
        "id": 38,
        "title": "Den verkliga utgången",
        "text": "Du ignorerar den öppna porten och går istället mot den plats där spegeln visade en stängd dörr.\n\n"
                "När du sträcker ut handen glider dörren upp ljudlöst. En kall vind sveper in – den här gången är det verkligt.\n\n"
                "Du har hittat den verkliga vägen ut ur slottet!",
        "options": [
            {"text": "Stig ut i friheten", "next_id": 40},
        ],
    },
    {
        "id": 39,
        "title": "Fångad i spegelvärlden",
        "text": "Du rör vid spegeln, och plötsligt sugs du in i en värld av reflektioner. Allting är omvänt, "
                "och korridoren verkar ändlös.\n\n"
                "Du har fastnat i spegelvärlden...",
        "options": [
            {"text": "Försök hitta en väg tillbaka", "next_id": 41},
        ],
    },
    {
        "id": 40,
        "title": "Frihet!",
        "text": "Du kliver ut i nattens kyliga luft. Slottet tornar upp sig bakom dig, dess mörka korridorer nu bara "
                "ett minne.\n\n"
                "Du är fri. Men frågan kvarstår – varför var du fast här från början?\n\n"
                "Detta mysterium återstår att lösas...",
        "options": [],
    },
    {
        "id": 41,
        "title": "Spegelvärldens evighet",
        "text": "Du försöker hitta en väg ut, men spegelvärlden verkar oändlig. Du går och går, men kommer ingenstans...\n\n"
                "Kanske fanns det ett annat val du borde ha gjort. Tiden går... och du förloras i reflektionerna för alltid.",
        "options": []
    },
    {
        "id": 41,
        "title": "Spegelvärldens evighet",
        "text": "Du försöker hitta en väg ut, men spegelvärlden verkar oändlig. "
                "Varje steg du tar speglas tillbaka på dig själv, och tiden känns som om den står stilla.\n\n"
                "Plötsligt ser du en reflektion av dig själv – men den rör sig inte som du gör. "
                "Det är en skugga av dig själv som stirrar tillbaka.",
        "options": [
            {"text": "Närma dig reflektionen", "next_id": 42},
            {"text": "Vända dig om och springa", "next_id": 43},
        ],
    },
    {
        "id": 42,
        "title": "Reflektionens gåta",
        "text": "När du närmar dig reflektionen börjar den tala med din egen röst:\n\n"
                "'Du är fångad, men jag är fri. Om du vill byta plats, lös min gåta:'\n\n"
                "'Jag är aldrig stilla, men jag går aldrig någonstans. Jag speglar alla, men har inget eget liv. Vad är jag?'",
        "options": [
            {"text": "En skugga", "next_id": 44},
            {"text": "En reflektion", "next_id": 45},
            {"text": "Tid", "next_id": 46},
        ],
    },
    {
        "id": 43,
        "title": "Evig flykt",
        "text": "Du springer genom spegelvärlden, men korridorerna bara fortsätter i oändlighet. "
                "Du ser dörrar och skuggor, men inget leder någonstans.\n\n"
                "Tillslut blir du utmattad... och inser att du är fast här för evigt.",
        "options": [
            {"text": "Allt upprepas, och du går vilse i evighet...", "next_id": 43},
        ],
    },
    {
        "id": 44,
        "title": "Fel svar...",
        "text": "'Fel!' ekar din röst tillbaka. Spegelvärlden skakar, och plötsligt är du ensam igen.\n\n"
                "Reflektionen har försvunnit, och du har ingen väg ut.",
        "options": [
            {"text": "Försök igen", "next_id": 42},
        ],
    },
    {
        "id": 45,
        "title": "Den rätta lösningen",
        "text": "Du viskar: 'En reflektion.'\n\n"
                "Spegelvärlden skakar till, och skuggan ler. 'Du förstår nu. Du är fri.'\n\n"
                "Plötsligt kastas du bakåt genom en virvel av ljus...",
        "options": [
            {"text": "Vakna upp i korridoren", "next_id": 36},
        ],
    },
    {
        "id": 46,
        "title": "Fel svar...",
        "text": "'Fel!' ekar din röst tillbaka. Spegelvärlden verkar krympa, och reflektionen ler hånfullt.\n\n"
                "Du har förlorat din chans att fly.",
        "options": [
            {"text": "Försök igen", "next_id": 42},
        ],
    },
]
