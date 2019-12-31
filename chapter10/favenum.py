import json

numfile = 'json_files/favenum.json'

def writenum(writefile):
    """Write the favorite number of the user."""
    favenum = input("What is your favorite number? ")
    with open(writefile, 'w') as f_obj:
        json.dump(favenum, f_obj)
    return favenum



def readnum(readfile):
    """Read the favorite number of the user."""
    try:
        with open(readfile) as f_obj:
            favenum = json.load(f_obj)
    except FileNotFoundError:
        pass
    else:
        return favenum


def favoritenum(inputfile):
    bestnum = readnum(inputfile)
    if bestnum:
        print("I know your favorite number! It is " + str(bestnum))
    else:
        bestnum = writenum(inputfile)
        print("We will save your favorite number as " + bestnum + ".")
    print("Thank you for your time.")

favoritenum(numfile)
