toppings = []
pizzaorder = "\nPlease enter a topping."
pizzaorder += "\nWhen you are done, please type 'done'."

more = True

while more:
    topping = input(pizzaorder)
    if topping == 'done':
        more = False
    toppings.append(topping)
    print("We have added " + topping + " to your list of toppings")
    

print(toppings)
