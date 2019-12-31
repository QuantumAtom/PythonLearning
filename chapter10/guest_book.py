guest = " "
guestbook = 'text_files/guest_book.txt'

while (guest != "exit"):
    guest = input("Please enter your name in our guest book: ")
    with open(guestbook, 'a') as guestentry:
        if (guest == "exit"):
            print("Exiting guest book")
        else:
            guestentry.write(guest + "\n")
            print("Thank you " + guest + " for visiting our hotel. We hope we make your stay here as comfortable as possible.")
