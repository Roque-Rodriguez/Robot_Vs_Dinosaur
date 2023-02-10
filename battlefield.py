from robot import *
from dinosaur import * 
from weapon import *

class Battlefeild:

    def __init__(self):
        self.robot = Robot("Terminator", Weapon)
        self.dinosaur = Dinosaur("Godzilla", 20)
        self.weapon = Weapon("Shotgun", 20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f"Thank you for comiing to watch {self.robot.name} take on {self.dinosaur.name}! LET THE GAMES BEGIN!!!!!!")
        print("Here are the rules: Each fighter will have 100 health and will use thier ability as best as they can to drop the opponent to 0.")

    def battle_phase(self):
       
       while self.robot.health <= 0:
            self.robot.attack(dinosaur)
            print(f"{self.name} hit {self.dinosaur.name} and has {self.dinosaur.health} left.")

       while self.dinosaur.health <= 0:
            self.dinosaur.attack(robot)
            print(f"{self.name} hit {self.robot.name} and has {self.robot.health} left.")

      
      
      
      
      
      
        # if self.robot.health == 0:
        #     self.robot.attack(dinosaur)
        #     print(f"{self.name} hit {self.dinosaur.name} and has {self.dinosaur.health} left.")
        # if self.dinosaur.health == 0:
        #     self.dinosaur.attack(robot)
        #     print(f"{self.name} hit {self.robot.name} and has {self.robot.health} left.")

    # def display_winner(self):


            


        # def removing_money(self, cash, player_one, player_two):
        # if self.cash <= cash:
        #     print(f'{self.name} does not have enough funds for this transaction.')
        # else:
        #     player_one.cash -= cash
        #     player_two.cash += cash
