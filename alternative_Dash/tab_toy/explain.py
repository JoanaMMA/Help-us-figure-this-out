# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:38:28 2020

@author: xXJaneXx
"""
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app_toy import HDapp

layout = [dcc.Markdown("""

#### The Project Goal and Data
Safve Heart is a Clinical Support System (CSS) designed to help clinicians predict heart disease (1). 
This project was be developed by Health Informatics students for Karolinska Institutet and Stockholm University 
over the course of 8 weeks and based on datasets from 
the Cleveland Clinic Foundation, 
the Hungarian Institute of Cardiology, 
de V.A. Medical Center and the University of Zurich (2)

###data


#### The Data and Evaluation Protocol


#### Model Selection

""")]