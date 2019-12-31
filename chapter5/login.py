users = []
if users:
    for login in users:
        if login == "admin":
            print("Would you like to see the log file?")
        else:
            print("This is PC has legal restrictions. Please see the lawyer.txt file.")
else:
    print("No users available for login.")
