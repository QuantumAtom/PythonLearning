import json
import geojson

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Get that data!

fn = '/home/marc/Documents/Development/Python/chapter16/2ndhw/data/all_day.geojson'

with open(fn) as datafile:
	EarthQData = json.load(datafile)

datatitle = (EarthQData['metadata']['title'])

EarthQDict = EarthQData['features']

mags, longs, lats, infotext = [], [], [], []

for EQData in EarthQDict:
	mags.append(EQData['properties']['mag'])
	longs.append(EQData['geometry']['coordinates'][0])
	lats.append(EQData['geometry']['coordinates'][1])
	infotext.append(EQData['properties']['place'])

#print(mags, longs, lats, infotext)

visualsetup = [{
	'type':'scattergeo',
	'lon':longs,
	'lat':lats,
	'text':infotext,
	'marker': {
		'size':[5*mag for mag in mags],
		'color':'mags',
		'colorscale':'Electric',
		'reversescale':False,
		'colorbar':{'title': 'New Data'},

	}
}]

caption = Layout(title=datatitle)
fig = {'data': visualsetup, 'layout': caption}
offline.plot(fig, filename='NewEQData.html')



