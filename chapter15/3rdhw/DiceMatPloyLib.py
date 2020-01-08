import matplotlib

import die

DieRoll = die()
DieRollResult = []

for roll_num in range(1000): #Roll the die 1000 times
	RollEm = DieRoll.roll() #Rollling the die and storing each result
	DieRollResult.append(RollEm) #Adding result to array
	