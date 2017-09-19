class Hero:
    def __init__(self, health, power):
        self.health = 10
        self.power = 5
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do {} damage to the goblin.".format(hero_power))
        if goblin.health <= 0:
            print("The goblin is dead.")

class Goblin:
    def __init__(self, health, power):
        self.health = 6
        self.power = 2
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if hero.health <= 0:
            print("You are dead.")
