#generic character class for both hero and goblin to inherit
class Character:
    def __init__(self, name):
        self.name = name
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

#new hero and goblin classes inheriting 'Character' class
class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 4
