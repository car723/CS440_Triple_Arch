# Data Layer

import json
import os

SAVE_FILE = "save.json"

class GameData:
    def __init__(self):
        self.score = 0
        self.click_value = 1

    def save(self):
        with open(SAVE_FILE, "w") as f:
            json.dump(self.__dict__, f)

    def load(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                self.score = data["score"]
                self.click_value = data["click_value"]
            return True
        return False