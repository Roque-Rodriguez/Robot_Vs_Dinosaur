from weapon import *
from dinosaur import *
import random

class Robot():

    def __init__(self,name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon("Shotgun", (random.randrange(1,25)))

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} pumps his {self.weapon.name} and shoots taking {self.weapon.attack_power} from {dinosaur.name}, lowing his health to: {dinosaur.health}")
    
        
        
       