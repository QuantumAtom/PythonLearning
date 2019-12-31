whereto = {}

asking = True

while asking:
    name = input("\nWhat is your name? ")
    where = input("\nWhere do you want to go? ")
    whereto[name] = where
    again = input("\nWill someone else be responding (Yes/No) ")
    again = again.lower()
    if again == "no":
        asking = False

for name, where in whereto.items():
    print(name + " would like to go to " + where + ".")
