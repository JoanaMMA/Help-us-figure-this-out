# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 09:47:22 2020

@author: xXJaneXx
"""


from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app_toy import HDapp

layout = [dcc.Markdown("""
### Project and Product Overview 
Safve Heart is a Clinical Support System (CSS) designed to help clinicians predict heart disease (1). 
This project was be developed by Health Informatics students for Karolinska Institutet and Stockholm University
over the course of 8 weeks and based on datasets from the Cleveland Clinic Foundation, 
the Hungarian Institute of Cardiology, 
de V.A. Medical Center and the University of Zurich (2). 

#### Business Needs 
Cardiovascular Disease (CVD) is one of the biggest causes of death nowadays(3). 
Considering that most CVDs could be prevented by premature detection 
and assessment of risk factors for early behavioural intervention(3,4),
a CDSS based on data mining would allow clinician to get a quicker deferential diagnosis (4). 
Considering that most healthcare organization aim to provide high quality 
services at an affordable rate (5), 
by creating a predictive system for early detection of CVD this project will 
be helping not only clinicians identify and address patients at risk, 
here by improving the quality of care given to said patients, but also,
 organizations by minimizing the need for excessive medical testing(6–8). 

 
""")]