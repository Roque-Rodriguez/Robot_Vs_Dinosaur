
class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = ""
        self.attack_power = 20
        self.health = 100

    def attack(self, robot):
        while self.health <= 0:
            print(f'{self.name} attacked {robot} with {self.weapon}')
            robot.health -= self.attack_power


     