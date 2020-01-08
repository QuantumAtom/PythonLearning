import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go
import numpy as nm




l = 500
x_steps = nm.random.choice([-1, 1], size = l) + 0.1 * nm.random.randn(l) # l steps
y_steps = nm.random.choice([-1, 1], size = l) + 0.1 * nm.random.randn(l) # l steps
x_position = nm.cumsum(x_steps) # integrate the position by summing steps values
y_position = nm.cumsum(y_steps) # integrate the position by summing steps values

#class walktheline(go, nm):

	# def __init__(self, go, nm):
	# 	self.x_move = 0	#combining how many steps in x axis and in what direction
	# 	self.x_steps = 0 #how many steps on the x axis
	# 	self.x_direct = 0 #whether to move right (1) or left (-1) on the x axis
	# 	self.y_move = 0 #combining how many steps in the y axis and in what direction
	# 	self.y_steps = 0 #how many steps to take on the y axis
	# 	self.y_direct = 0 #whether to move up (1) or down (-1) on the y axis
	# 	self.data = []
	
	# def xaxis(self, go, nm):
	# 	self.x_steps = nm.random.randint(1, 6)
	# 	self.x_direct = [-1,1][random.randrange(2)]
	# 	self.x_move = self.x_steps * self.x_direct
	
	# def yaxis(self, go, nm):
	# 	self.y_steps = nm.random.randint(1, 6)
	# 	self.y_direct = [-1,1][random.randrange(2)]
	# 	self.y_move = self.y_steps * self.y_direct
	

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='Random Walk',
        figure = go.Figure(data=go.Scatter(
			x = x_position,
			y = y_position,
			mode = 'markers',
			name = 'I walk the line (many of them)',
			marker = dict(
				color = nm.arange(500),
				size = 8,
				colorscale = 'Electric',
				showscale = True
			)

		))
            


            
        
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)