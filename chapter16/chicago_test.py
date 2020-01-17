import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/chicago_weather_2020.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header, in enumerate(header_row):
		print(index, column_header)
		