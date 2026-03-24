from data import GameData
from logic import GameLogic
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
            break

if __name__ == "__main__":
    main()