#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:27:49 2019

@author: matildalif
"""
import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)

params = ['#games','W', 'L', 'P']
players = ['Mathias', 'Tim', 'Juha', 'David', 'Ola']

app.layout = html.Div([
    dash_table.DataTable(
        id='pingis-table',
        columns=(
            [{'id': 'Player', 'name': 'Player'}] +
            [{'id': p, 'name': p} for p in params]
        ),
        data = [dict(Player=players[i-1], 
                     **{param: 0 for param in params}) for i in range(1,len(players)+1)],        
        editable=True,
        style_cell={
            'whiteSpace': 'no-wrap',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': 0,
            },
    )
])  


if __name__ == '__main__':
    app.run_server(debug=True)
