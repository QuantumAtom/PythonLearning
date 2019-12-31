my_foods = ["pizza", 'falafel', 'carrot cake']
#This will not work
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("My friend's favorite foods are: ")
print(friend_foods)

for yummy in my_foods:
    print(yummy)

for icky in friend_foods:
    print(icky)