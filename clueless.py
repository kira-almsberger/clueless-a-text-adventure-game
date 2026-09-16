# Final Group Project
# Due 5/3/26
# JT King, Kira Almsberger, Shane Mallory, Marcus Ferguson

import random

# ==========================
# Instructions function
# ==========================
def show_instructions():
    print("\nWelcome to Clueless! A classic murder mystery case.")
    print("\nSearch the mansion to collect clues and interview suspects.")
    print("Some clues are useful, but some may be misleading.")
    print("Use your notebook to compare clues with each suspect.")
    print("Once you think you know the answer, make your accusation.\n")


# ======================
# Main menu function
# ======================
def main_menu():
    while True:
        print("\nGame Start Menu")
        print("Select one of the following:")
        print("1 - Play the Game")
        print("2 - Show Instructions")
        print("3 - Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nPut your detective hat on! Game starting!")
            play_game()
        elif choice == "2":
            show_instructions()
        elif choice == "3":
            print("Thanks for playing. Ending the game.")
            break
        else:
            print("Invalid choice.")


# ======================================================
# Setting up Mystery / Randomized Aspect of the Game
# ======================================================
def create_suspects():
    return {
        "Miss Scarlet": {
            "hair": "red",
            "accessory": "gold ring",
            "weapon": "Knife",
            "statement": "I was nowhere near the kitchen tonight.",
        },
        "Colonel Mustard": {
            "hair": "gray",
            "accessory": "medal",
            "weapon": "Wrench",
            "statement": "I heard a heavy object hit the floor near the library.",
        },
        "Professor Plum": {
            "hair": "brown",
            "accessory": "glasses",
            "weapon": "Lead Pipe",
            "statement": "Someone rushed past me carrying something long and metal.",
        },
        "Mrs. Peacock": {
            "hair": "black",
            "accessory": "blue scarf",
            "weapon": "Rope",
            "statement": "I saw a shadow moving toward the ballroom.",
        },
        "Mr. Green": {
            "hair": "blonde",
            "accessory": "cufflinks",
            "weapon": "Revolver",
            "statement": "I stayed in the hall after I heard the scream.",
        },
    }


def setup_mystery():
    suspects = create_suspects()
    killer = random.choice(list(suspects.keys()))
    traits = suspects[killer]

    important_clues = [
        f"a strand of {traits['hair']} hair",
        f"a dropped {traits['accessory']}",
        f"the {traits['weapon']} used in the crime",
    ]

    decoy_clues = create_decoy_clues(suspects, killer)
    return killer, suspects, important_clues, decoy_clues


def create_decoy_clues(suspects, killer):
    decoys = []

    for name, traits in suspects.items():
        if name != killer:
            decoys.append(f"a loose {traits['accessory']}")
            decoys.append(f"a note mentioning the {traits['weapon']}")

    random.shuffle(decoys)
    return decoys[:4]


# =============
# Room Data
# =============
def create_rooms(important_clues, decoy_clues, suspects):
    searchable_rooms = ["room1", "room3", "room4", "room6", "room7", "room8", "room9"]
    clue_rooms = random.sample(searchable_rooms, 3)
    decoy_rooms = [room for room in searchable_rooms if room not in clue_rooms]

    suspect_names = list(suspects.keys())
    random.shuffle(suspect_names)

    rooms = {
        "room1": {
            "name": "Study",
            "desc": "Dust lines the bookshelves. A polished desk sits by the window, and something shiny catches your eye.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room2", "room4"],
        },
        "room2": {
            "name": "Hall",
            "desc": "The main hall stretches through the mansion. Every sound seems to echo here.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room1", "room3", "room5"],
        },
        "room3": {
            "name": "Lounge",
            "desc": "The lounge smells strongly of perfume. A few cushions have been knocked out of place.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room2", "room6"],
        },
        "room4": {
            "name": "Library",
            "desc": "Tall shelves line the walls. A few books are scattered on the floor like someone left in a hurry.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room1", "room5", "room7", "room8"],
        },
        "room5": {
            "name": "Pool",
            "desc": "The pool room smells like chlorine. The water is still, but wet footprints mark the tile.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room2", "room4", "room6", "room8"],
        },
        "room6": {
            "name": "Dining",
            "desc": "A long table is set perfectly. One chair is pulled back, and a napkin lies crumpled underneath it.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room3", "room5", "room8", "room9"],
        },
        "room7": {
            "name": "Garden",
            "desc": "The indoor garden is humid and quiet. The plants are thick enough for someone to hide behind.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room4", "room8"],
        },
        "room8": {
            "name": "Ballroom",
            "desc": "Spotlights shine across the wide dance floor. A large curtain hangs against the far wall.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room4", "room5", "room6", "room7", "room9"],
        },
        "room9": {
            "name": "Kitchen",
            "desc": "The kitchen is spotless except for one messy counter. A knife block sits near the large island.",
            "clue": None,
            "suspect": None,
            "connected_rooms": ["room6", "room8"],
        },
    }

    for i, room_key in enumerate(clue_rooms):
        rooms[room_key]["clue"] = important_clues[i]

    for i, room_key in enumerate(decoy_rooms):
        if i < len(decoy_clues):
            rooms[room_key]["clue"] = decoy_clues[i]

    i = 0
    for room_key in rooms:
        if room_key != "room2":
            rooms[room_key]["suspect"] = suspect_names[i % len(suspect_names)]
            i += 1

    return rooms


# =================================================
# Game Play - Function to handle clue collection
# =================================================
def collect_clue(room_key, rooms, found_clues, notebook):
    room = rooms[room_key]

    if room["clue"]:
        print(f"You found: {room['clue']}")
        choice = input("Do you want to pick up the clue? (Enter 'y' for yes): ").lower()

        if choice == "y":
            found_clues.append(room["clue"])
            notebook["clues_found"].append(room["clue"])
            room["clue"] = None
            print("Clue added to your notebook!")
        else:
            print("You leave the clue where it is.")
    else:
        print("You searched this room, but found nothing new.")


# ==============================================
# Game Play - Function to move between rooms
# ==============================================
def move_room(current, rooms):
    print("\nConnected rooms:")
    for r in rooms[current]["connected_rooms"]:
        print(f"- {rooms[r]['name']}")

    choice = input("Where to?: ").strip().lower()

    for r in rooms[current]["connected_rooms"]:
        if choice == rooms[r]["name"].strip().lower():
            return r

    print("Invalid room choice. Staying in current room.")
    return current


def interview_suspect(room, suspects, notebook):
    suspect = room["suspect"]

    if not suspect:
        print("There is no suspect here to interview.")
        return

    print(f"\nYou interview {suspect}.")
    print(f'"{suspects[suspect]["statement"]}"')
    notebook["suspects_seen"][suspect] = suspects[suspect]


# ================================================
# Game Play - Function for accusing guilty party
# ================================================
def accuse(suspects, killer):
    print("\nMake your accusation:")
    names = list(suspects.keys())

    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

    try:
        pick = int(input("Enter number: "))
        if 1 <= pick <= len(names):
            guess = names[pick - 1]
        else:
            print("Invalid number.")
            return False
    except ValueError:
        print("Invalid input.")
        return False

    if guess == killer:
        print(f"\nCorrect! {killer} is guilty.")
        return fight(killer)

    print(f"\nWrong! {guess} is innocent.")
    return False


# ================================================
# Game Play - Function for fighting guilty party
# ================================================
def fight(killer):
    print(f"\nBut wait! {killer} refuses to go down without a fight!")
    print("The door is locked and there is no escape.")
    print(f"You and {killer} square up.")

    player_health = 20
    enemy_health = 15

    while player_health > 0 and enemy_health > 0:
        print(f"\nYour Health: {player_health} | {killer}'s Health: {enemy_health}")
        action = input("Do you want to attack? (y/n): ").strip().lower()

        if action == "y":
            print(f"\nYou attack {killer}.")
            damage = random.randint(2, 5)
            enemy_health -= damage
            enemy_health = max(0, enemy_health)
            print(f"You deal {damage} damage. {killer} has {enemy_health} health left!")

            if enemy_health <= 0:
                print(f"\n{killer} is knocked out. Case closed!")
                return True

            damage2 = random.randint(1, 4)
            player_health -= damage2
            player_health = max(0, player_health)
            print(f"\n{killer} attacks you!")
            print(f"You take {damage2} damage. You have {player_health} health left!")

            if player_health <= 0:
                print(f"\nYou have been defeated by {killer}. They run loose in the mansion.")
                return False
        else:
            print(f"You tried to run away, but {killer} catches you.")
            print(f"You lose the fight and {killer} runs free in the mansion.")
            return False

    return False


# ====================================
# Item / Inventory functions
# ====================================
ITEM_DETAILS = {
    "red hair": ("Red Hair", "Appearance: Bright red strand.", "Special: Might have fallen from someone with red hair."),
    "gray hair": ("Gray Hair", "Appearance: Thin gray strand.", "Special: Might have fallen from someone with gray hair."),
    "brown hair": ("Brown Hair", "Appearance: Dark brown strand.", "Special: Might have fallen from someone with brown hair."),
    "black hair": ("Black Hair", "Appearance: Smooth black strand.", "Special: Might have fallen from someone with black hair."),
    "blonde hair": ("Blonde Hair", "Appearance: Light blonde strand.", "Special: Might have fallen from someone with blonde hair."),
    "ring": ("Gold Ring", "Appearance: Shiny engraved ring.", "Special: Identifies its owner."),
    "medal": ("Medal", "Appearance: Military-style medal.", "Special: Belongs to a decorated suspect."),
    "glasses": ("Glasses", "Appearance: Thin framed glasses.", "Special: Belongs to someone studious."),
    "scarf": ("Blue Scarf", "Appearance: Soft blue fabric.", "Special: Identifies its owner."),
    "cufflinks": ("Cufflinks", "Appearance: Polished silver pair.", "Special: Identifies its owner."),
    "knife": ("Knife", "Appearance: Sharp steel blade.", "Special: Possible murder weapon."),
    "wrench": ("Wrench", "Appearance: Heavy metal tool.", "Special: Could cause serious harm."),
    "lead pipe": ("Lead Pipe", "Appearance: Thick metal pipe.", "Special: Looks like it might hurt."),
    "rope": ("Rope", "Appearance: Strong braided rope.", "Special: Could restrain victims."),
    "revolver": ("Revolver", "Appearance: Small handgun.", "Special: Extremely dangerous weapon."),
}


def inspect_clue(clue):
    clue_lower = clue.lower()

    for keyword, details in ITEM_DETAILS.items():
        if keyword in clue_lower:
            print(f"\n{details[0]}")
            print(details[1])
            print("Value: No money value in this case.")
            print(details[2])
            return

    print("\nUnknown clue.")


def show_suspect_notes(notebook):
    print("\nSuspects encountered:")
    if notebook["suspects_seen"]:
        for s_name, traits in notebook["suspects_seen"].items():
            print(f"- {s_name}: {traits['hair']} hair, wearing {traits['accessory']}, known weapon: {traits['weapon']}")
    else:
        print("None yet.")


def show_clue_notes(notebook):
    print("\nClues collected:")
    if notebook["clues_found"]:
        for i, clue in enumerate(notebook["clues_found"], 1):
            print(f"{i}. {clue}")
    else:
        print("No clues collected yet.")


def inventory(notebook):
    while True:
        print("\n--- Inventory / Notebook ---")
        print("1 - View suspects encountered")
        print("2 - View clues collected")
        print("3 - Inspect a clue")
        print("4 - Exit notebook")
        choice = input("Choice: ")

        if choice == "1":
            show_suspect_notes(notebook)
        elif choice == "2":
            show_clue_notes(notebook)
        elif choice == "3":
            show_clue_notes(notebook)
            if not notebook["clues_found"]:
                continue

            clue_choice = input("\nSelect clue number to inspect (Enter to cancel): ")
            if clue_choice == "":
                continue
            if clue_choice.isdigit():
                clue_number = int(clue_choice)
                if 1 <= clue_number <= len(notebook["clues_found"]):
                    inspect_clue(notebook["clues_found"][clue_number - 1])
                else:
                    print("Invalid number.")
            else:
                print("Invalid input.")
        elif choice == "4":
            print("----------------------------\n")
            return
        else:
            print("Invalid choice.")


# ====================================
# Map
# ====================================
screen = None
painter = None

room_map = {
    "room1": (-200, -150, 100, 100, "Study"),
    "room2": (-100, -150, 200, 100, "Hall"),
    "room3": (100, -150, 100, 100, "Lounge"),
    "room4": (-200, -50, 100, 150, "Library"),
    "room5": (-100, -50, 200, 100, "Pool"),
    "room6": (100, -50, 100, 150, "Dining"),
    "room7": (-200, 100, 100, 100, "Garden"),
    "room8": (-100, 50, 200, 150, "Ballroom"),
    "room9": (100, 100, 100, 100, "Kitchen"),
}


def setup_map():
    global screen, painter

    if screen is not None and painter is not None:
        return True

    try:
        import turtle

        screen = turtle.Screen()
        screen.setup(width=600, height=600)
        screen.title("Mansion Map")
        screen.tracer(0)

        painter = turtle.Turtle()
        painter.hideturtle()
        painter.speed(0)
        painter.penup()
        return True
    except Exception as error:
        print(f"\nThe map window could not be opened: {error}")
        print("You can still play the game using the room names in the menu.")
        return False


def show_map(current):
    if not setup_map():
        return

    painter.clear()

    for key, (x, y, w, h, name) in room_map.items():
        painter.goto(x, y)
        painter.setheading(0)
        painter.pendown()

        for _ in range(2):
            painter.forward(w)
            painter.left(90)
            painter.forward(h)
            painter.left(90)

        painter.penup()
        painter.goto(x + w / 2, y + 10)
        painter.write(name, align="center")

        if key == current:
            painter.goto(x + w / 2, y + h / 2)
            painter.dot(20, "red")
            painter.write("YOU", align="center", font=("Arial", 10, "bold"))

    screen.update()
    print("\nMansion Map updated.")


def important_clues_found(found_clues, important_clues):
    total = 0

    for clue in important_clues:
        if clue in found_clues:
            total += 1

    return total


# ====================================
# Play Game Function / Game Loop
# ====================================
def play_game():
    killer, suspects, important_clues, decoy_clues = setup_mystery()
    rooms = create_rooms(important_clues, decoy_clues, suspects)

    found_clues = []
    current = "room2"

    notebook = {
        "suspects_seen": {},
        "clues_found": [],
    }

    while True:
        room = rooms[current]
        print(f"\nYou are in the {room['name']}.")
        print(room["desc"])

        if room["suspect"]:
            suspect = room["suspect"]
            print(f"\nYou see {suspect} here.")
            print(f"They have {suspects[suspect]['hair']} hair and are wearing a {suspects[suspect]['accessory']}.")

            if suspect not in notebook["suspects_seen"]:
                notebook["suspects_seen"][suspect] = suspects[suspect]

        print("\n1 - Search for a clue")
        print("2 - Move to another room")
        print("3 - Interview suspect")
        print("4 - Open Inventory / Notebook")
        print("5 - View Map")
        print("6 - Make an accusation")
        print("7 - Quit to menu")
        choice = input("\nChoice: ")

        if choice == "1":
            collect_clue(current, rooms, found_clues, notebook)
        elif choice == "2":
            current = move_room(current, rooms)
        elif choice == "3":
            interview_suspect(room, suspects, notebook)
        elif choice == "4":
            inventory(notebook)
        elif choice == "5":
            show_map(current)
        elif choice == "6":
            if important_clues_found(found_clues, important_clues) < 2:
                print("\nYou do not have enough solid evidence yet. Keep investigating.")
            else:
                won = accuse(suspects, killer)
                if won:
                    print("\nYou solved the case!")
                else:
                    print("\nGame over.")
                break
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

        if important_clues_found(found_clues, important_clues) == 3:
            print("\nYou have found enough strong evidence to solve the case.")
            print("\n--- Case Notebook ---")
            show_suspect_notes(notebook)
            show_clue_notes(notebook)
            print("---------------------\n")

            choice = input("Do you want to make an accusation? (Enter 'y' for yes and 'n' for no): ").lower()
            if choice == "y":
                won = accuse(suspects, killer)
                if won:
                    print("\nYou solved the case!")
                else:
                    print("\nGame over.")
                break


# =======
# Start
# =======
if __name__ == "__main__":
    main_menu()
