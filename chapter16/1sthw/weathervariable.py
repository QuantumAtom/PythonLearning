import csv

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches


from datetime import datetime

sitka_date = []
sitka_high = []
sitka_low = []

dv_date = []
dv_high = []
dv_low = []

sf_date = []
sf_high = []
sf_low = []

d = 0
h = 0
l = 0

fileimport = ''

dateformat = '%m/%d/%Y'

location = ''


def records(fileimport, d, h, l, dateformat):
	filename = fileimport

	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		for index, column_header, in enumerate(header_row):
			print(index, column_header)

		for row in reader:
			locale = str(row[1])
			print(location)
			break

		#Get date, and high and low temperatures from this file.
		dates, highs, lows = [], [], []
		for row in reader:
			current_date = datetime.strptime(row[d], dateformat)
			high = int(row[h])
			low = int(row[l])
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	return dates, highs, lows, locale



sitka_date, sitka_high, sitka_low, sitka_locale = records('data/sitka_weather_2018_simple.csv', 2, 5, 6, '%Y-%m-%d')

dv_date, dv_high, dv_low, dv_locale = records('data/death_valley_2018_simple.csv', 2, 4, 5, '%m/%d/%Y')

sf_date, sf_high, sf_low, sf_locale = records('data/sf_weather_2018.csv', 2, 3, 4, '%Y-%m-%d')

def graphplot(d, h, l, location, technicolor):
	#Plot the high and low temperatures.
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(d, h, c=technicolor, alpha=0.5)
	ax.plot(d, l, c=technicolor, alpha=0.5)
	plt.fill_between(d, h, l, facecolor=technicolor, alpha=0.1)

	#Format plot.
	plt.title("Daily high and low temperatures - 2018\n" + location, fontsize=24)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)

	plt.show()	


graphplot(sitka_date, sitka_high, sitka_low, sitka_locale, 'blue')
graphplot(dv_date, dv_high, dv_low, dv_locale, 'red')
graphplot(sf_date, sf_high, sf_low, sf_locale, 'green')