from weapon import *
from dinosaur import *

class Robot():

    def __init__(self,name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon("Shotgun", 20)

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(dinosaur.health)
        
        
        # while self.health > 0:
            # dinosaur.health -= self.weapon.attack_power
            # print(Dinosaur.health)


#   self.power_level -= 10
#             dinosaur_to_attack.health -= self.weapon.attack_power
#             print(f'{self.name} power level is now {self.power_level}')
#             print(f'{dinosaur_to_attack.type} health is now {dinosaur_to_attack.health}')