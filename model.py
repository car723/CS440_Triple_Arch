# Model

import json
import os

SAVE_FILE = "save.json"

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

    def save(self):
        with open(SAVE_FILE, "w") as f:
            json.dump({
                "score": self.score,
                "click_value": self.click_value
            }, f)

    def load(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                self.score = data["score"]
                self.click_value = data["click_value"]
            return True
        return False