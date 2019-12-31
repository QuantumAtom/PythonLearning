faveplaces = {
    'anthony': {
        'restaurant': 'dennys',
        'hangout': 'galloping ghost',
        'landmark': 'wrigley field',         
    },

    'mj': {
        'restaurant': 'ullas',
        'hangout': 'charlies',
        'landmark': 'boystown pylons',
    },   

    'beth': {
        'restaurant': 'the buffalo',
        'hangout': 'shapiro house',
        'landmark': 'daley plaza',
    },

}   

for person, places in faveplaces.items():
    print(str(person) + str(places))
    eats = places['restaurant']
    hang = places['hangout']
    historic = places['landmark']
    print(person + " like to go to " + str(eats), str(hang), str(historic))