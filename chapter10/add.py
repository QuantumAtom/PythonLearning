thing1 = ''
thing2 = ''

while(thing1 or thing2 != "exit"):

    thing1 = input("What is your first number?") 
    if (thing1 == "exit"):
        break

    thing2 = input("What is your second number?")
    if (thing2 == "exit"):
        break

    try:
        suessical = int(thing1) + int(thing2)
    except ValueError:
        print("That's not a number")
    else:
        print(suessical)