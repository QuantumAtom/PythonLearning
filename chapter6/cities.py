cities = {

    'tel aviv': {
        'country': 'israel',
        'population': 429000,
        'fact': 'It has one of the largest Jewish populations in the world.',
    },

    'singapore': {
        'country': 'singapore',
        'population': 5607000,
        'fact': 'It is one of the few city-states in the world.',
    },

    'london': {
        'country': 'united kingdom',
        'population': 8788000,
        'fact': 'It is an alpha world city.',
    },
}

for city, info in cities.items():
    location = info['country']
    people = info['population']
    note = info['fact']
    print("\nThe city is: " + city.title())
    print("The city is located in: " + location.title() + ".")
    print("There are " + str(people) + " in the city.")
    print("Fun fact: " + note)