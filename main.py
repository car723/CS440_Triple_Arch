# main.py (Monolithic)

import json
import os

SAVE_FILE = "save.json"

score = 0
click_value = 1

def show_menu():
    print("\n--- Clicker Game ---")
    print(f"Score: {score}")
    print("1. Click")
    print("2. Buy Upgrade (+1 per click) [Cost: 10]")
    print("3. Save Game")
    print("4. Load Game")
    print("5. Exit")

def main():
    global score, click_value

    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            score += click_value

        elif choice == "2":
            if score >= 10:
                score -= 10
                click_value += 1
                print("Upgrade purchased!")
            else:
                print("Not enough points!")

        elif choice == "3":
            save_game()

        elif choice == "4":
            load_game()

        elif choice == "5":
            break

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

def save_game():
    data = {
        "score": score,
        "click_value": click_value
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("Game saved!")

def load_game():
    global score, click_value
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            score = data["score"]
            click_value = data["click_value"]
        print("Game loaded!")
    else:
        print("No save file found.")