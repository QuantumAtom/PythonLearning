from collections import Counter

import matplotlib.pyplot as plt

from die import Die

DieRoll = Die() #Rolling the dice
DieRollResult = [] #Array of the results
DieCountAll = [] #Array of the count of the results
DieSides = []
DieSidesCount = 1
DieCountSum = []

DieRollMax = DieRoll.num_sides + 1

while DieSidesCount < DieRollMax:
	DieSides.append(DieSidesCount)
	DieSidesCount = DieSidesCount + 1

for roll_num in range(1000): #Roll the die 1000 times
	RollEm = DieRoll.roll() #Rollling the die and storing each result
	DieRollResult.append(RollEm) #Adding result to array

DieCountAll = Counter(DieRollResult) #Count each side was landed on
print(DieCountAll)
DieCountAllSort = list(dict(sorted(DieCountAll.items())).values())
print(DieCountAllSort)


print(DieCountSum)

# for num in range(1, DieRoll.num_sides + 1):
# 	DieCount = Counter(num)
# 	DieCountAll.append(DieCount)

x = DieSides #Counting each number on the die
y = DieCountAllSort #Counting how many of each number on the die

print(x)
print(y)
print(type(y))

#Luck be a lady tonight!
plt.bar(x, y, label = 'Count of die rolls', color = '#7851a9')
plt.title("Viva Las Vegas!")
plt.show()




