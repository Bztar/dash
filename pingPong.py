# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:00:24 2019

@author: mbackstr
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

columns=['name','W','L','P']

def generate_table(columns, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in columns])] +
        # Body
        [html.Tr([html.Td(['Mathias']), html.Td(id='Mathias')]),
        html.Tr([html.Td(['Tim']), html.Td(id='Tim')]),
        html.Tr([html.Td(['Juha']), html.Td(id='Juha')]),
        html.Tr([html.Td(['David']), html.Td(id='David')]),
        html.Tr([html.Td(['Ola']), html.Td(id='Ola')])]
    )

app.layout = html.Div(children=[
    html.H4(children='Pingis Table'),
    generate_table(columns),
    dcc.Input(
        id='Player1',
        type='number',
        value=0
    ),
    dcc.Input(
        id='Player2',
        type='text',
        value='JANNEFUCKINGHELLBOM'
    )
])

@app.callback(
    [Output('Mathias', 'children'),
     Output('Tim', 'children'),
     Output('Juha', 'children'),
     Output('David', 'children'),
     Output('Ola', 'children')],
    [Input('Player1', 'value')])
def callback_a(x):
    return x, x, x, x, x

if __name__ == '__main__':
    app.run_server(debug=True)

