
#Marc Freiman's long term goals

goals = ['Finish the house', 'Find a lifepartner', 'Move up doing server/cloud admin or development', 'Save for retirement', 'Stop giving into my id']
print(goals)

print(goals[0])
print(goals[1])
print(goals[2])
print(goals[3])
print(goals[4])

print("I hope to " + goals[0] + " by the end of next year.")

print(goals[1].title())
print(goals[2].upper())
print(goals[3].lower())
print(goals[-1])

goals.append('Be more social')
print(goals)
goals.insert(3, "Change my diet and exercise")
print(goals)
del goals[3]
print(goals)
goalpop = goals.pop()
print(goalpop)
print(goals)
popgoal = goals.pop(3)
print(popgoal)
goals.remove('Finish the house')
print(goals)

goals.sort()
print(goals)
goals.sort(reverse=True)
print(goals)

print(sorted(goals))

goals.reverse
print(goals)

finale = len(goals)
print(finale)