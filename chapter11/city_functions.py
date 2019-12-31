def location(city, country, population = ''):
    if population:
        locale = city.title() + ", " + country + " - population " + str(population)
    else:
        locale = city.title() + ", " + country
    return locale

ChileanCapital = location('santiago', 'Chile', 50000000)

print(ChileanCapital)


    