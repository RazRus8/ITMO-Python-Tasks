import time
import random

class Fighter:
    hp = 100

    def __init__(self, name):
        self.name = name

    def Hit(self, unit):
        if unit.hp > 0:
            unit.hp -= 20
            print(self.name, " hits ", unit.name, " for 20 hp!")
            time.sleep(0.5)
            print(unit.name, " has ", unit.hp, " hp left!\n")
            time.sleep(2)
        
        if unit.hp == 0:
            print(str(self.name) + " wins! Fatality...")


f1 = Fighter("Subzero")
f2 = Fighter("Scorpion")

while(f1.hp > 0 and f2.hp > 0):
    rnd = random.randint(0, 1)

    if rnd == 0:
        f1.Hit(f2)
    else:
        f2.Hit(f1)