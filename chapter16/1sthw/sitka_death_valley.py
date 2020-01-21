import csv

import matplotlib.pyplot as plt

from datetime import datetime

sitka_date = []
sitka_high = []
sitka_low = []

dv_date = []
dv_high = []
dv_low = []


def sitka_records(dates, high, low):
	filename = 'data/sitka_weather_2018_simple.csv'

	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		for index, column_header, in enumerate(header_row):
			print(index, column_header)
			
		#Get date, and high and low temperatures from this file.
		dates, highs, lows = [], [], []
		for row in reader:
			current_date = datetime.strptime(row[2], '%Y-%m-%d')
			high = int(row[5])
			low = int(row[6])
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

def dv_records(dates, high, low):
	filename = 'data/death_valley_2018_simple.csv'

	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		for index, column_header, in enumerate(header_row):
			print(index, column_header)
			
		#Get date, and high and low temperatures from this file.
		dates, highs, lows = [], [], []
		for row in reader:
			current_date = datetime.strptime(row[2], '%Y-%m-%d')
			high = int(row[4])
			low = int(row[5])
			dates.append(current_date)
			highs.append(high)
			lows.append(low)



sitka_records(sitka_date, sitka_high, sitka_low)

dv_records(dv_date, dv_high, dv_low)

print(dv_high)
print(dv_low)

#Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sitka_date, sitka_high, c='blue', alpha=0.5)
ax.plot(sitka_date, sitka_low, c='blue', alpha=0.5)
plt.fill_between(sitka_date, sitka_high, sitka_low, facecolor='blue', alpha=0.1)
ax.plot(dv_date, dv_high, c='red', alpha=0.5)
ax.plot(dv_date, dv_low, c='red', alpha=0.5)
plt.fill_between(dv_date, dv_high, dv_low, facecolor='red', alpha=0.1)





#Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()