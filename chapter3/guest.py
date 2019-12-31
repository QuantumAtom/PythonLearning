guests = ['Albert Einstein', 'Bill Clinton', 'Yitzhak Rabin', 'Rosalind Franklin', 'George Washington', 'Golda Meier', 'Andrew Carnegie']
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[0] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[1] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[2] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[3] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[4] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[5] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[6] + " that we will enjoy ourselves. Thank you.")

print(guests[3])
del guests[3]
guests.insert(3, "Angela Merkel")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[0] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[1] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[2] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[3] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[4] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[5] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[6] + " that we will enjoy ourselves. Thank you.")

print("I found more suitable seating for all us " + str(guests) + ". So I am sure we can fit three more people.")
guests.insert(0, 'Bill Maher')
guests.insert(5, 'Jon Stewart')
guests.append('Ellen Sirleaf')
print(guests)
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[0] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[1] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[2] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[3] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[4] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[5] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[6] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[7] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[8] + " that we will enjoy ourselves. Thank you.")
print("You are cordinally invited to join me in a dinner party. I am sure " + guests[9] + " that we will enjoy ourselves. Thank you.")

print(len(guests))


cancelled = guests.pop(0)
print("I am sorry " + cancelled + ", but I will have to cancel the invite and I want to reschedule with you.")

cancelled = guests.pop(0)
print("I am sorry " + cancelled + ", but I will have to cancel the invite and I want to reschedule with you.")
cancelled = guests.pop(0)
print("I am sorry " + cancelled + ", but I will have to cancel the invite and I want to reschedule with you.")
cancelled = guests.pop(2)
print("I am sorry " + cancelled + ", but I will have to cancel the invite and I want to reschedule with you.")
cancelled = guests.pop(2)
print("I am sorry " + cancelled + ", but I will have to cancel the invite and I want to reschedule with you.")
cancelled = guests.pop(2)
print("I am sorry " + cancelled + ", but I will have to cancel the invite and I want to reschedule with you.")
cancelled = guests.pop(2)
print("I am sorry " + cancelled + ", but I will have to cancel the invite and I want to reschedule with you.")
cancelled = guests.pop(2)
print("I am sorry " + cancelled + ", but I will have to cancel the invite and I want to reschedule with you.")

print(guests)
del guests[0]
del guests[0]

print(guests)

