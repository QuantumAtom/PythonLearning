import json
import geojson

#Get that data!

fn = '/home/marc/Documents/Development/Python/chapter16/2ndhw/data/all_day.geojson'

with open(fn) as datafile:
	EarthQData = json.load(datafile)

formatfile = '/home/marc/Documents/Development/Python/chapter16/2ndhw/data/FormattedEQData.geojson'

with open(formatfile, 'w') as filewrite:
	json.dump(EarthQData, filewrite, indent=4)