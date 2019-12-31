from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Store the results in a list
results = []

#Set the variable names of the dice
die_1 = Die(8)
die_2 = Die(8)

#Roll them like Vegas
for roll_num in range(1000):
	roll_total = die_1.roll() + die_2.roll()
	results.append(roll_total)

#Bookie analysis

#Set variable for frequency of results
Vegas_Odds = []

#Set max results for dice roll return value
maxresults = die_1.num_sides + die_2.num_sides

#Count de Money (or dice rolls!)
for dice_value in range(2, maxresults+1):
	frequency = results.count(dice_value)
	Vegas_Odds.append(frequency)

#Set values for gambling board
roll_values = list(range(2, maxresults+1))
freq_roll = [Bar(x=roll_values, y=Vegas_Odds)]

x_ax_config = {'title':'Dice Roll', 'dtick':1}
y_ax_config = {'title':'How often it rolls'}

#Laying it all out for ya
gamble_spread = Layout(title='The Bellagio dice board', xaxis=x_ax_config, yaxis=y_ax_config)

offline.plot({'data':freq_roll, 'layout': gamble_spread}, filename='doubleD8.html')


