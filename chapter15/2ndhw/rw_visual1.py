import matplotlib.pyplot as plt

import numpy as nm

from random import randrange

while True:
	x_values = []
	y_values = []

	count = 0

	#Generate x-axis plot points
	while(count <=5):
		plotpoints = randrange(5000)
		x_values.append(plotpoints)
		count += 1

	count = 0

	while(count <=5):
		plotpoints = randrange(5000)
		y_values.append(plotpoints)
		count += 1

	#Plot the points in the list
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15, 9))
	ax.plot(x_values, y_values, linewidth=1)

	#Remove the axes
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another plot? (y/n): ")
	if keep_running == "n":
		break