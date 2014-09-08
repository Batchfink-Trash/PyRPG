from time import sleep
from random import randint
import pickle



class Player(object):

    def __init__(self, gender, race, name):
        self.gender = gender
        self.race = race.lower()
        self.name = name

        global health
        health = 20
        global player_base_attack
        player_base_attack = 0
        global inventory
        inventory = {"Gold":50, "Training sword":1, }
        global potions
        potions = 0

        if self.race == "dwarf":
            player_base_attack = 2
        elif self.race == "elf":
            player_base_attack = 1
        elif self.race == "human":
            player_base_attack == 2
        else:
            player_base_attack == 1



    def attack(self):
        global enemy_health
        global player_base_attack
        enemy_health -= player_base_attack + randint(1, 3)

    def description(self):
        print("I'm a %s %s called %s" % (self.gender, self.race, self.name))

    def pickup_item(self, item):
        global inventory
        inventory.update(item)

    
    def health_potion(self):
        global potions
        global health
        if(0 < potions):
            health += 5
            print("Health: %s" %(health))
            potions -= 1
        else:
            print("You need a health potion to do that!")




class Enemy(object):
    def __init__(self, name, enemy_base_attack, base_defence):
        self.name = name
        self.enemy_base_attack = enemy_base_attack
        self.base_defence = base_defence

    def attack(self):
        global health
        damage = self.enemy_base_attack + randint(1, 3)
        health -= damage
        print("")
        print("The %s hit for %s health" %(self.name, damage))
        print("Health: %s" % health)
        print("")
        if health <= 0:
            end_game()

def end_game():
    if health < 0:
        print("Oh no! You appear to be REALLY dead! Goodbye")
        exit
    else:
        print("Oh no!  You appear to be dead! Goodbye!")
        exit

gender = input("Gender: ")
race = input("Race: ")
name = input("Name: ")

player = Player(gender, race, name)

player.description()


print("")
print("An orc attacks!")
sleep(1)
orc = Enemy("Orc", 1, 2)
orc.attack()
sleep(1)
player.pickup_item({"Orc Flesh":1})
print("Inventory: " + str(inventory))

with open("savegame", "wb") as f:
    print("Saving game...")
    pickle.dump(player, f, protocol=2)
    print("Done!")

player.race = "elf"
player.pickup_item({"Gold bar":3})

with open("savegame", "rb") as f:
    print("loading game")
    pickle.load(f)
    print("Done!")

player.description()
print(inventory)