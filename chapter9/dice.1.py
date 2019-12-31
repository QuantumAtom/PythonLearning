from random import randint

class Die():
    
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die6(self):
        sides = randint(1, 6)
        return sides

die1 = Die()
die2 = Die()


result1 = die1.roll_die6()
result2 = die2.roll_die6()

result = result1 + result2

print(result)




    

