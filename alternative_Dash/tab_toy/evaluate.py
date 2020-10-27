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

#### Classification Evaluation \
A variety of well-known classifiers were discussed, after the individual work of several students, we have concluded to use the following three classifiers. \
Random forest classifier + Random Search Cross-validation has the following results of evaluation\
SVM + Random Search CV\
Logistic regression\
The required  evaluation metrics: precision, recall, f1-score, accuracy, AUC + Confusion matrix. \
Final decision: Cleveland Data with logistic regression \

#### other suggestions
Processed data in two different ways \
Model 1: Cleveland data, one-hot encoding \
Model 2: All four datasets, normalisation \
Chose different classifiers \
Support vector machine \
Random Forest \
Logistic regression \
Employed different models \ 
The two models above, classified from 0-4 \
Model 3: Cleveland data, classified 0 and 1 \  
""")]
# fig of metrics and plots
