# Model

class GameModel:
    def __init__(self):
        self.score = 0
        self.click_value = 1

    def click(self):
        self.score += self.click_value

    def buy_upgrade(self):
        if self.score >= 10:
            self.score -= 10
            self.click_value += 1
            return True
        return False