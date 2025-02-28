# För att importera berättelsen från en annan fil så använder vi from <filnamn> 
# import <variabel> och sedan kan vi använda variabeln i vår kod. I det här 
# fallet så har vi importerat berättelsen från redbutton.py och döpt om 
# variabeln till BOOK. Vi kan nu använda variabeln BOOK för att komma åt 
# berättelsen i vår kod. Det är viktigt att den heter BOOK (det är därför vi använder
# as BOOK) för det är variabeln som används i vår kod.
# from book import BOOK
from my_adventure import adventure as BOOK
import json

def player_input(prompt):
    while True:
        choice = input(prompt)

        try:
            if choice == "i":
                if len(inventory) == 0:
                    print("Ditt inventory är tomt")
                
                else:
                    print("Ditt inventory:")

                    for i in range(0, len(inventory)):
                        print(f"{i + 1}. {inventory[i]}")
            
            elif type(int(choice)) == int:
                return int(choice)
            
            else:
                print("Skriv in ett nummer eller 'i' för att öppna ditt inventory.")
        
        except ValueError:
            print("Skriv in ett nummer eller 'i' för att öppna ditt inventory.")

# Funktion get_page som tar två argument, book_data och page_id. Den går igenom
# varje sida i book_data och om sidans id matchar page_id så returnerar den sidan.
def get_page(book_data, page_id):
    for page in book_data:
        if page["id"] == page_id:
            return page
        
    return None

# Funktion show_page som tar en sida som argument och skriver ut titeln, texten
# och varje alternativ på sidan.
def show_page(page):
    print(page["title"])
    print(page["text"])

    for i, option in enumerate(page["options"]):
        print(f"{i + 1}. {option['text']}")

inventory = []
loaded_id = [0]

# Main är huvudfunktionen som körs när programmet startas.
def main():
    current_id = loaded_id[0]

    with open("savegame.json", "r") as f:
        savedata = json.load(f)

    save_count = len(savedata) + 1

    while True and current_id is not None:
        current_page = get_page(BOOK, current_id)
        show_page(current_page)

        if current_id in [40, 41]:
            current_id = None

        if "loot" in current_page:
            print(f"Du hittade {current_page['loot']}!")

            if current_page["loot"] not in inventory:
                inventory.append(current_page["loot"])
                
                if save_count <= len(savedata):
                    savedata[save_count]["Inventory"] = inventory

                with open("savegame.json", "w") as f:
                    json.dump(savedata, f, indent = 4)

        while True:
            choice = player_input("Vad gör du?\n> ")

            if current_id == 0 and current_page["options"][choice - 1]["next_id"] == -1:
                if savedata == {}:
                    print("Du har inga sparade spel")
                
                else:
                    print(f"Du har {len(savedata)} sparade spel")

                    try:
                        save_choice = int(input("Vilken omgång vill du ladda?\n> "))
                        load(save_choice)
                    
                    except ValueError:
                        print("Skriv in en siffra istället.")
            
            else:
                break

        if 1 <= choice <= len(current_page["options"]):
            current_id = current_page["options"][choice - 1]["next_id"]

            if current_page["options"][0]["next_id"] == 1:
                savedata[save_count] = {}

                with open("savegame.json", "w") as f:
                    json.dump(savedata, f, indent = 4)

                savedata[save_count]["Choices"] = []

                with open("savegame.json", "w") as f:
                    json.dump(savedata, f, indent = 4)

            if current_id - 1 != 0:
                try:
                    savedata[save_count]["Choices"].append(choice - 1)
                
                except KeyError:
                    savedata[str(save_count - 1)]["Choices"].append(choice - 1)

                with open("savegame.json", "w") as f:
                    json.dump(savedata, f, indent = 4)

        else:
            print("Det går inte. Försök igen.")

def load(save):
    with open("savegame.json", "r") as f:
        savedata = json.load(f)

    saved_game = str(save)

    for item in savedata[saved_game]["Inventory"]:
        inventory.append(item)

    current_id = 1
    current_choice_index = 0

    while True:
        if current_choice_index >= len(savedata[saved_game]["Choices"]):
            loaded_id[0] = current_id
            main()
        
        else:
            current_choice = savedata[saved_game]["Choices"][current_choice_index]
            current_page = get_page(BOOK, current_id)
            current_id = current_page["options"][current_choice]["next_id"]
            current_choice_index += 1

if __name__ == "__main__":
    main() # starta main-funktionen