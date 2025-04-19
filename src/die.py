class Die:
    id = 0
    __init__(self, sides: int):
    self.sides = sides
    self.id = Die.id
    Die.id += 1
    currentSide = 1

    def printStatus(self):
        print(f"Die id #{self.id}")
        print(f"Number of sides: {self.sides}")
        print(f"Side up: {self.currentSide}")



