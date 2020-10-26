# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:38:29 2020

@author: xXJaneXx
"""

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app_toy import HDapp

layout = [dcc.Markdown("""
### Final Results
The predictions were 

""")]
# fig of metrics and plots