def pets(petlist):
    try:
        with open(petlist) as furry:
            meowbarks = furry.read()
    except FileNotFoundError:
        pass
    else:
        print(meowbarks)

FreimanPets = ['text_files/cats.txt', 'text_files/dogs1.txt']

for petnames in FreimanPets:
    pets(petnames)