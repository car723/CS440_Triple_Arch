# Business Logic Layer

class GameLogic:
    def __init__(self, data):
        self.data = data

    def click(self):
        self.data.score += self.data.click_value

    def buy_upgrade(self):
        if self.data.score >= 10:
            self.data.score -= 10
            self.data.click_value += 1
            return True
        return False
    
    def save_game(self):
        self.data.save()

    def load_game(self):
        return self.data.load()