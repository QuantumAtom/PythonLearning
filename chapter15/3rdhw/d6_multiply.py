from plotly.graph_objs import Bar, Layout
from plotly import offline
import numpy

from die import Die

#Store the results in a list
results = []

#Set the variable names of the dice
die_1 = Die()
die_2 = Die()

dice = [die_1, die_2]
dice_num = len(dice)

#dice = [Die() for _ in range(N)]

#Roll them like Vegas
for roll_num in range(1000):
	roll_count = []
	for d in dice:
		roll_total = d.roll()
		roll_count.append(roll_total)
	roll_sum = numpy.prod(roll_count)
	results.append(roll_sum)

#Bookie analysis

#Set variable for frequency of results
Vegas_Odds = []

sides_results = []

#Set max results for dice roll return value
for d in dice:
	dice_num_side = d.num_sides
	sides_results.append(dice_num_side)

sides_sum = sum(sides_results)
maxresults = die_1.num_sides*die_2.num_sides
minresults = dice_num
print(maxresults)

#Count de Money (or dice rolls!)
for dice_value in range(dice_num, maxresults+1):
	frequency = results.count(dice_value)
	Vegas_Odds.append(frequency)

#Set values for gambling board
roll_values = list(range(dice_num, maxresults+1))
freq_roll = [Bar(x=roll_values, y=Vegas_Odds)]

x_ax_config = {'title':'Dice Roll', 'dtick':1}
y_ax_config = {'title':'How often it rolls'}

#Laying it all out for ya
gamble_spread = Layout(title='The Bellagio dice board', xaxis=x_ax_config, yaxis=y_ax_config)

offline.plot({'data':freq_roll, 'layout': gamble_spread}, filename='dice_roll.html')


