import matplotlib.pyplot as plot

plot.style.use('fivethirtyeight')

fivethoucubed = round(5000**(1/3))

countednumbers = list(range(5001))
cubednumbers = [x**3 for x in countednumbers]

dom, cubes = plot.subplots()

cubes.scatter(countednumbers, cubednumbers, c=cubednumbers, cmap=plot.cm.plasma, s=100)

cubes.set_title("Cube Numbers", fontsize=24)
cubes.set_xlabel("Count", fontsize=14)
cubes.set_ylabel("Cubed Numbers", fontsize=14)

cubes.tick_params(axis='both', which='major', labelsize=14)

cubes.axis([0, 5100, 0, 5100**3])

plot.show()