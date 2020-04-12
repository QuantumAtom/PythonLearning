import dash

import dash_core_components as dcc

import dash_html_components as html

from dash.dependencies import Input, Output

import plotly.graph_objects as go

from operator import itemgetter

import requests


#Make an API call and store the response

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Process information about each submission

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
	#Make a seperate API call for each submission
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	#Build a dictionary for each article.
	submission_dict = {
		'title': response_dict['title'],
		'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
		'comments': response_dict['descendants'],
	}

	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)




#Dash components
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='Hacker News Enthusiasm',
        figure={
            go.figure([go.Bar(x=submission_dicts.title, y=submission_dicts.comments)])
			fig.show
            }
        }
    )
])

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
