from RPG_2 import Hero, Goblin, Medic, Shadow
#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

gonzo = Hero()
pol_pot = Goblin()
medic = Medic()
shadow = Shadow()

def main(hero, enemy):
    while enemy.alive() > 0 and hero.alive() > 0:
        print("\n")
        hero.print_status()
        enemy.print_status()
        print("\nWhat do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive() > 0:
            enemy.attack(hero)

main(gonzo, pol_pot)