class Hero:
    def __init__(self, health, power):
        self.health = 10
        self.power = 5
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do {} damage to the goblin.".format(hero_power))
        if goblin.health <= 0:
            print("The goblin is dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        while self.health > 0:
            print("You have {} health and {} power.".format(hero_health, hero_power))

class Goblin:
    def __init__(self, health, power):
        self.health = 6
        self.power = 2
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if hero.health <= 0:
            print("You are dead.")
    def alive(self):
        if self.helth > 0:
            return True
        else:
            return False
    def print_status(self):
        while self.health > 0:
            print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
