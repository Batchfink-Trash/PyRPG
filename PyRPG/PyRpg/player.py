class Player(object):
    """The Player instance"""
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



