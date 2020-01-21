import csv

import matplotlib.pyplot as plt

from datetime import datetime

datafile = 'data/sitka_weather_2018_simple.csv'

#Open the file and let's go
with open(datafile) as d:
	readfile = csv.reader(d)
	headrow = next(readfile)
	
	#The table of contents
	for index, column_header in enumerate(headrow):
		print(index, column_header)

	#Store data
	rainfall = []
	dates = []

	#Store the data by looping through the data in the CSV file
	for row in readfile:
		date = datetime.strptime(row[2], '%Y-%m-%d')
		rainamt = float(row[3])
		dates.append(date)
		rainfall.append(rainamt)

	#Due diligence checking
	print(dates)
	print(rainfall)

#Let's make data art!
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='#006994')

#Format the plotted chart
title = "Daily rainfall\nSitka, AK\n2018"
plt.title(title, fontsize=18)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Rainfall", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()


