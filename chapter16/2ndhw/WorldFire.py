import csv

from plotly.graph_objs import Scattergeo, Layout

from plotly import offline

firefile = '/home/marc/Documents/Development/Python/chapter16/2ndhw/data/MODIS_C6_Global_24h.csv'

with open(firefile) as filevar:
	FireData = csv.reader(filevar)
	hrow = next(FireData)

	for indexnum, cheader in enumerate(hrow):
		print (indexnum, cheader)

	lat, long, bright = [], [], []
	for row in FireData:
		latfl = float(row[0])
		longfl = float(row[1])
		brightfl = float(row[2])

		lat.append(latfl)
		long.append(longfl)
		bright.append(brightfl)

visinfo = [{
	'type':'scattergeo',
	'lon':long,
	'lat':lat,
	'marker':{
		'color': bright,
		'colorscale':'Magma',
		'reversescale':False,
		'colorbar':{'title': 'Fires Brightness'}
	}
}]

caption = Layout(title="World Fires")
fig = {'data':visinfo, 'layout': caption}
offline.plot(fig, filename='WorldFires.html')