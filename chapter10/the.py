


def CountThe(book):
    try:
        with open(book) as classics:
            words = classics.read()
    except FileNotFoundError:
        print("We do not have that in our collections.")
    else:
        CountThe = words.lower().count('the')
        return CountThe
    
collection = ['text_files/treasureisland.txt', 'text_files/aesop.txt', 'text_files/sherlock.txt']

for literature in collection:
    NumberThe = CountThe(literature)
    print("The word 'the' appears " + str(NumberThe) + " times in '" + literature + "' .")