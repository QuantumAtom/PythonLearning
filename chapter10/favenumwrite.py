import json

#Get the user's favorite number and store in a JSON file.

numberfile = 'json_files/favenum.json'
FavInt = input("What is your favorite number?")
with open(numberfile, 'w') as j_obj:
    json.dump(FavInt, j_obj)

print("I know your favorite number! It's " + str(FavInt))