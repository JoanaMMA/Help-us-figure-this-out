# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:38:10 2020
this is based on the guidence from https://jimking100.github.io/2019-12-08-Post-7/

The Dash App
Our basic Dash app is composed of the app.py and the index.py files.
@author: xXJaneXx
"""

import dash
import dash_bootstrap_components as dbc

HDapp = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#HDapp.config.suppress_callback_exceptions = True
server = HDapp.server


