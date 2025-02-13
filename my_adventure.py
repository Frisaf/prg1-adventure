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
]
