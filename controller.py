# Controller

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.display(self.model.score)
            choice = self.view.get_input()

            if choice == "1":
                self.model.click()

            elif choice == "2":
                if self.model.buy_upgrade():
                    self.view.show_message("Upgrade purchased!")
                else:
                    self.view.show_message("Not enough points!")

            elif choice == "3":
                self.model.save()
                self.view.show_message("Game saved!")

            elif choice == "4":
                if self.model.load():
                    self.view.show_message("Game loaded!")
                else:
                    self.view.show_message("No save file found.")

            elif choice == "5":
                break