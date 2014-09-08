class Enemy(object):
    """Enemy base class"""
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