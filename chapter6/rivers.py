rivers = {
    'Mississippi': 'United States',
    'Rio Grande': 'United States/Mexico',
    'Ganges': 'India',
}

for water, country in rivers.items():
    print("The " + water + " runs through " + country + ".")

for water in rivers.keys():
    print(water)

for country in rivers.values():
    print(country)