import json

#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it

def get_stored_username():
    """Get stored username if available."""
    filename = 'json_files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'json_files/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    current_username = input("Who is the person using this system? ")
    if (username and username == current_username):
            print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
        
greet_user()