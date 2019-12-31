def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

#greet_user('jesse')
#greet_user('sarah')

#This is an infinite loop!
while True:
    print("\nPlease tell me your full name: ")
    print("\nPlease enter 'q' at any time to quit.")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")