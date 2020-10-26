# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:42:11 2020
this is based on the guidence from https://jimking100.github.io/2019-12-08-Post-7/

The Dash App
The app.py file simply initializes and instantiates the app
The index.py file is the main executable for the app.
@author: xXJaneXx
"""



import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

#from folder_name import (file or module)
from app_toy import HDapp
from tab_toy import intro, predict , explain, evaluate, references

style={'border': 'thin black solid',
        'textAlign': 20,
        'backgroundColor': 'white',
        'color': 'black',
        'font-size': 20,
        'maxWidth': 'Auto', 
        'margin': 'auto'}

HDapp.layout = html.Div([
    html.Div([html.H2('Safve Heart',
                      style={'marginLeft': 20, 'color': 'white'}
                     ),
              html.H3('A Predictive Clinical Support System for Heart Disease',
                      style={'marginLeft': 25, 'color': 'white'})
             ],
             style={'border': 'thin black solid',
                    'backgroundColor': '#d61519',
                    'padding': '10px 5px'}),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Intro', value='tab-intro'),
        dcc.Tab(label='Predict', value='tab-predict'),
        dcc.Tab(label='Explain', value='tab-explain'),
        dcc.Tab(label='Evaluate', value='tab-evaluate'),
        dcc.Tab(label='References', value='tab-references')
    ]),
    html.Div(id='tabs-content'),
],style=style)

@HDapp.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-predict': return predict.layout
    elif tab == 'tab-explain': return explain.layout
    elif tab == 'tab-evaluate': return evaluate.layout
    elif tab == 'tab-references': return references.layout


if __name__ == '__main__':
    HDapp.run_server()