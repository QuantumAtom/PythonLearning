def show_magicians(wizards):
    for magicman in wizards:
        print (magicman)

def make_great(wizards):
    great = []
    while wizards:
        magicman = wizards.pop()
        magical = str(magicman) + " The Great!"
        great.append(magical)
    return(great)




sorcerers = ['Merlin', 'Houdini', 'Harry Potter']
mastercraft = []

show_magicians(sorcerers)
mastercraft = make_great(sorcerers[:])
show_magicians(sorcerers)
show_magicians(mastercraft)

