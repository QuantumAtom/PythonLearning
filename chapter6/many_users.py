users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    #Print user name
    print("\nUsername: " + username)
    
    #Enter values into variables
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    #Print values
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
