pizza = ["cheese pizza", "jalapeno pizza", "deep dish pizza"]

for slices in pizza:
    print("I ate so much " + slices + " that I can barely move.")

print("We Chicagoans LOVE pizza!")

friend_pizza = pizza[:]

pizza.append('hot pepper pizza')
friend_pizza.append('onion pizza')

for pizzatype in pizza:
    print(pizzatype)

for friendpizzatype in friend_pizza:
    print(friendpizzatype)