guest = input("Please enter your name in our guest book: ")
guestbook = "text_files/guest.txt"

with open(guestbook, 'w') as guestentry:
    guestentry.write(guest)
