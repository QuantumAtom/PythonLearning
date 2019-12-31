def make_pizza(size, *toppings):
    """The function is called make_pizza. It summarize the pizza we are about to make. It takes the size and toppings as arguments and 
    will print the pizza."""
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

