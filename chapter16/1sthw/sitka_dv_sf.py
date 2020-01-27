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


def records(fileimport, d, h, l, dateformat):
	filename = fileimport

	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		for index, column_header, in enumerate(header_row):
			print(index, column_header)
			
		#Get date, and high and low temperatures from this file.
		dates, highs, lows = [], [], []
		for row in reader:
			current_date = datetime.strptime(row[d], dateformat)
			high = int(row[h])
			low = int(row[l])
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	return dates, highs, lows



sitka_date, sitka_high, sitka_low = records('data/sitka_weather_2018_simple.csv', 2, 5, 6, '%Y-%m-%d')

dv_date, dv_high, dv_low = records('data/death_valley_2018_simple.csv', 2, 4, 5, '%m/%d/%Y')

sf_date, sf_high, sf_low = records('data/sf_weather_2018.csv', 2, 3, 4, '%Y-%m-%d')

#Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sitka_date, sitka_high, c='blue', alpha=0.5)
ax.plot(sitka_date, sitka_low, c='blue', alpha=0.5)
plt.fill_between(sitka_date, sitka_high, sitka_low, facecolor='blue', alpha=0.1)
ax.plot(dv_date, dv_high, c='red', alpha=0.5)
ax.plot(dv_date, dv_low, c='red', alpha=0.5)
plt.fill_between(dv_date, dv_high, dv_low, facecolor='red', alpha=0.1)
ax.plot(sf_date, sf_high, c='green', alpha=0.5)
ax.plot(sf_date, sf_low, c='green', alpha=0.5)
plt.fill_between(dv_date, dv_high, dv_low, facecolor='green', alpha=0.1)

#Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

sitka_label = mpatches.Patch(color='blue', label='Sitka Data')
dv_label = mpatches.Patch(color='red', label='Death Valley Data')
sf_label = mpatches.Patch(color='green', label='San Francisco Data')
plt.legend(handles=[sitka_label, dv_label, sf_label])

plt.show()