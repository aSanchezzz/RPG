import random

#generic character class for both hero and goblin to inherit
class Character:
    def __init__(self):
        self.name = ''
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, enemy):
        print("\n{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)

    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.\n".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

#new hero and goblin classes inheriting 'Character' class
class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 50
        self.power = 5
    def attack(self, enemy):
        if random.randint(1,2) == 1:
            super().attack(enemy)
        else:
            print("\n{} attacks {} DOUBLE HIT".format(self.name, enemy.name))
            enemy.receive_damage(self.power * 2)

class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 50
        self.power = 5

class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 5
        self.power = 5
    def receive_damage(self, enemy):
        super(Medic, self).receive_damage(self.health)
        if random.randint(1, 2) == 1:
            self.health =+ 2

class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 1
        self.power = 2
    def receive_damage(self, points):
        if random.randint(1,10) == 1:
            super().receive_damage(points)
        else:
            print("{} DEFLECTED ATTACK!\n".format(self.name))