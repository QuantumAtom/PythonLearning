sandwich_orders =["Pastrami", "Mahi Reuben", "Pastrami", "PB&J", "Pastrami", "Cheese"]
finished_sandwiches = []
print("No Pastrami for you!")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    sammich = sandwich_orders.pop()
    print("An order of " + sammich + " coming up!")
    finished_sandwiches.append(sammich)

print(finished_sandwiches)