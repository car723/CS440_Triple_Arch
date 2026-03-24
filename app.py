from data import GameData
from logic import GameLogic
import logic
import presentation as ui

def main():
    data = GameData()
    logic = GameLogic(data)

    while True:
        ui.show_menu(data.score)
        choice = ui.get_input()

        if choice == "1":
            logic.click()

        elif choice == "2":
            if logic.buy_upgrade():
                print("Upgrade purchased!")
            else:
                print("Not enough points!")

        elif choice == "3":
            logic.save_game()
            print("Game saved!")

        elif choice == "4":
            if logic.load_game():
                print("Game loaded!")
            else:
                print("No save file found.")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()