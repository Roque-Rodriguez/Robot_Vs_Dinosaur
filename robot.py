from weapon import *


class Robot:

    def __init__(self,name, Weapon):
        self.name = ""
        self.health = 100
        self.weapon = Weapon

    def attack(self, dinosaur):
        while self.health <= 0:
            print(f'{self.name} attacked {dinosaur} with {self.weapon}')
            dinosaur.health -= self.weapon.attack_power
            print(self.dinosaur.health)