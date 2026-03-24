# View

class GameView:
    def display(self, score):
        print("\n--- Clicker Game ---")
        print(f"Score: {score}")
        print("1. Click")
        print("2. Buy Upgrade (+1 per click) [Cost: 10]")
        print("3. Save Game")
        print("4. Load Game")
        print("5. Exit")

    def get_input(self):
        return input("Choose: ")

    def show_message(self, message):
        print(message)