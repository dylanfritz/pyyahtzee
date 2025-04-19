import random

class Die:
    id = 0
    __init__(self, sides: int):
        self.sides = sides
        self.id = Die.id
        Die.id += 1
        self.currentSide = 1

    def printStatus(self):
        print(f"Die id #{self.id}")
        print(f"Number of sides: {self.sides}")
        print(f"Side up: {self.currentSide}")

    def roll(self):
        self.currentSide = random.randint(1,self.sides)
        return self.currentSide

    def setSide(self, num):
        assert num <= self.sides, "Cannot set die to side it does not have"
        self.currentSide = num



