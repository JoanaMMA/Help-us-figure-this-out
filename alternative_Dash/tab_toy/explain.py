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
Safve Heart is a Clinical Support System (CSS) designed to help clinicians predict heart disease (1). \ 
This project was be developed by Health Informatics students for Karolinska Institutet and Stockholm University 
over the course of 8 weeks \
based on datasets from the Cleveland Clinic Foundation, the Hungarian Institute of Cardiology, de V.A. Medical Center and the University of Zurich (2)

###data
Our first task related to become familiar with the data \
Processed both Cleveland exclusively, and all four datasets combined\ 

###Pre-processing
Used one-hot encoding for the categorical data. Variables are converted into a form that could be provided to ML algorithms to do a better job in prediction. \
For remaining continuous data, data was normalised, scaler, removing the mean and scaling the data to unit variance. \

###Tools 
Python + libraries \
Dash for interactive tool \
###Environments:
Jupyter Notebook and spyder
""")]
