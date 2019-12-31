import json

getfavenum = 'json_files/favenum.json'

with open(getfavenum) as jsonfiles:
    favenum = json.load(jsonfiles)

print("I know your favorite number! It is " + str(favenum))

