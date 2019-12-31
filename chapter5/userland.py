current_users = ["Freimanm", "rayc", "thompsonm", "kwongt", "callahanp"]
new_users = ["freimanm", "Vonbuscht", "thorrezp", "kwongt", "reyesa"]

for newbies in new_users:
    if newbies.lower() in current_users:
        print("User name has been taken. Please choose another.")
    else:
        print("User name is available")
