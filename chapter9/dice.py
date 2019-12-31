from random import randint

class Die():
    
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die6(self):
        sides = randint(1, 6)
        print(sides)

    def roll_die10(self):
        sides = randint(1, 10)
        print(sides)
    
    def roll_die20(self):
        sides = randint(1, 20)
        print(sides)

MGMGrand = Die()


count = 0

while(count<10):
    MGMGrand.roll_die6()
    count = count + 1

while(count<20):
    MGMGrand.roll_die10()
    count = count + 1

while(count<20):
    MGMGrand.roll_die20()
    count = count + 1

    

