import json
import geojson

#Get that data!

fn = '/home/marc/Documents/Development/Python/chapter16/2ndhw/data/all_day.geojson'

with open(fn) as datafile:
	EarthQData = json.load(datafile)

datatitle = (EarthQData['metadata']['title'])

mags, longs, lats, infotext = [], [], [], []

for EQData in EarthQData:
	print(EQData['properties']['mags'])
	mags.append(EQData['properties']['mags'])
	longs.append(EQData['geometry']['coordinates'][0])
	lats.append(EQData['geometry']['coordinates'][1])
	infotext.append(EQData['properties']['place'])

visualsetup = [{
	'type':'scattergeo',
	'lon':'longs',
	'lat':'lats',
	'text':'infotext',
	'marker': {
		'size':[5*mag for mag in mags],
		'color':'mags',
		'colorscale':'Electric',
		'reversescale':False,
		'colorbar':{'title': 'New Data'},

	}
}]

caption = layout(title=datatitle)
visualize = {'data': visualsetup, 'layout': caption}
offline.plot(visualize, filename='NewEQData.html')



