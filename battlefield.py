from robot import *
from dinosaur import * 
from weapon import *


class Battlefeild():

    def __init__(self):
        self.robot = Robot("Terminator", 100)
        self.dinosaur = Dinosaur("Godzilla", (random.randrange(1, 25)), 100)
        

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f"Thank you for comiing to watch {self.robot.name} take on {self.dinosaur.name}! LET THE GAMES BEGIN!!!!!!")
        print("Here are the rules: Each fighter will have 100 health and will use thier ability as best as they can to drop the opponent to 0.")

    def battle_phase(self):
       
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
            
     

    def display_winner(self):
        if self.robot.health > 1:
            print(f"{self.robot.name} is the winner.")
        elif self.dinosaur.health > 1:
            print(f"{self.dinosaur.name} is the winner")
