import random

class Mplayer:
    def __init__(self, newname):
        self.name = newname
        self.score = 0
        self.is_done = False
    
    def roll_dice(self):
        roll = random.randint(1, 6)
        self.score += roll
        return roll