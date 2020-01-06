import dash

import dash_core_components as dcc

import dash_html_components as html

import plotly.graph_objects as go

import numpy as nm
 
import random

class walking():

	def __init__(self, go, nm):
		self.x_move = 0	#combining how many steps in x axis and in what direction
		self.x_steps = 0 #how many steps on the x axis
		self.x_direct = 0 #whether to move right (1) or left (-1) on the x axis
		self.y_move = 0 #combining how many steps in the y axis and in what direction
		self.y_steps = 0 #how many steps to take on the y axis
		self.y_direct = 0 #whether to move up (1) or down (-1) on the y axis
		self.z_move = 0 #combining how many steps in z axis and in what direction
		self.z_steps = 0 #how many steps on the z axis
		self.z_direct = 0 #whether to move forward (1) or backwards (-1) on the z axis
		self.data = []
	
	def xaxis(self, go, nm):
		self.x_steps = nm.random.randint(1, 6)
		self.x_direct = [-1,1][random.randrange(2)]
		self.x_move = self.x_steps * self.x_direct
	
	def yaxis(self, go, nm):
		self.y_steps = nm.random.randint(1, 6)
		self.y_direct = [-1,1][random.randrange(2)]
		self.y_move = self.y_steps * self.y_direct
	
	def zaxis(self, go, nm):
		self.z_steps = nm.random.randint(1, 6)
		self.z_direct = [-1,1][random.randrange(2)]
		self.z_move = self.z_steps * self.z_direct
	
	def trace(self, go, nm):
		trace = go.Scatter3d(
			x = self.x_move,
			y = self.y_move,
			z = self.z_move,
			marker = dict({
				size : 2,
				opacity : 0.6,
				color :'aqua'	
			})
		)
		data.append(trace)


	def layout(self, go, nm):
		layout = go.layout(
			title = 'Fremont Street Walk',
			margin = dict(
				l=0,
				r=0,
				b=25,
				t=50
			),
			scene = dict(
				xaxis=dict(
					title='',
					autorange=True,
					showgrid=False,
					zeroline=False,
					showline=False,
					ticks='',
					showticklabels=False
				),
				yaxis=dict(
					title='',
					autorange=True,
					showgrid=False,
					zeroline=False,
					showline=False,
					ticks='',
					showticklabels=False
				),
				zaxis=dict(
					title='',
					autorange=True,
					showgrid=False,
					zeroline=False,
					showline=False,
					ticks='',
					showticklabels=False
				)
			)
		)

	def dash_server(self, go, nm, dash, dcc, html):
		external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

		app = dash.Dash(__name__, external_stylesheets)

		app.layout = html.Div(children=[
			html.H1(children='Dash Random Walk'),

			html.Div(children='''A masochistic attempt at using a framework I heard about two days ago.'''),

			dcc.Graph(
				id='Random walking after midnight',
				figure={
					'data' : self.data,
					'layout' : self.layout

				}
			)
		])
		if __name__ == '__main__':
			app.run_server(debug = True)
	
	def whole_thing(self, go, nm, dash, dcc, html):
		self.xaxis(go, nm)
		self.yaxis(go, nm)
		self.zaxis(go, nm)
		self.trace(go, nm)
		self.layout(go, nm)
		self.dash_server(go, nm, dash, dcc, html)

walking(go, nm).whole_thing(go, nm, dash, dcc, html)