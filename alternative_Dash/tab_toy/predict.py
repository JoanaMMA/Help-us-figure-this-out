import pandas as pd
import numpy as np
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from it_WORKS import model

from joblib import load
import pickle

from app_toy import HDapp, server


layout = html.Div([
    dcc.Markdown("""
        ### Predictive Clinical Support System
        Use the controls below to update your predicted risk for Heart Disease.
        The Patient has a predicted risk for Heart disease of:
    """),

    html.Div(id='patient_data'),

    html.Div("Demographics", style={'marginleft': 30,
                               'font-weight': 'bold',
                               'font-color': 'black',
                               'font-weight': 'bold',
                               'font-size': 20,
                               'textAlign': 'center'}),
           dbc.Row([dbc.Col(html.Div([
                   html.Label(children='Age(years): '),
                   dcc.Input(
                       type="number",
                       debounce=True,
                       value= 45.0,
                       id='age')]),
                    width={"size": 3}),   
               dbc.Col(html.Div([
                   html.Label(children='Sex:'),
                   dcc.Dropdown(
                       options=[
                           {'label': 'Female', 'value': 0.0},
                           {'label': 'Male', 'value': 1.0}
                       ],
                       value= 1.0,
                       id='sex'
                   )]),
                   width={"size": 3})],style={'padding': '10px 10px', 
                                               'Align': 'center'}),
   
       html.Div("Clinical Findings",
                         style={'marginleft': 30,
                               'font-weight': 'bold',
                               'font-color': 'black',
                               'font-weight': 'bold',
                               'font-size': 20,
                               'textAlign': 'center'}),

               dbc.Row([dbc.Col(html.Div([
                       html.Label(children='Chest Pain: '),
                       dcc.Dropdown(
                           options=[
                               {'label': 'Asymptomatic', 'value': 4.0 },
                               {'label': 'Typical Angina', 'value': 1.0},
                               {'label': 'Atypical Angina', 'value': 2.0},
                               {'label': 'Non-anginal', 'value': 3.0},
                           ],
                           value= 2.0,
                           id='cp'
                       )]), 
                       width={"size": 3})],style={'padding': '10px 10px', 
                                               'Align': 'center'}),
                dbc.Row([dbc.Col(html.Div([
                       html.Label(children='Systolic Blood Pressure (mmHg): '),
                       dcc.Input(
                           id='trestbps',
                           type="number",
                           debounce=True,
                           value= 120.0
                       )]), 
                       width='auto')],style={'padding': '10px 10px', 
                                               'Align': 'center'}),
             dbc.Row([dbc.Col(html.Div([
                       html.Label(children='Serum Cholesterol(mg/L): '),
                       dcc.Input(
                           id='chol',
                           type="number",
                           debounce=True,
                           value= 155.0
                       )]),
                       width='auto')],style={'padding': '10px 10px', 
                                               'Align': 'center'}),                              
            dbc.Row([dbc.Col(html.Div([
                       html.Label(children='Fasting blood sugar >120mg/dl:'),
                       dcc.Dropdown(
                           options=[
                               {'label': 'No', 'value': 0.0},
                               {'label': 'Yes', 'value': 1.0}
                           ],
                           value= 1.0,
                           id='fbs'
                       )]), 
                       width='auto')],style={'padding': '10px 10px', 
                                               'Align': 'center'}),
             dbc.Row([dbc.Col(html.Div([
                       html.Label(children='Resting ECG:'),
                       dcc.Dropdown(
                           options=[
                               {'label': 'Normal', 'value': 0.0},
                               {'label': 'ST alterations', 'value': 1.0},
                               {'label': 'LVH', 'value': 2.0}
                       ],
                       value= 0.0,
                       id='restecg'
                       )]),
                       width={"size": 3})],style={'padding': '10px 10px'}),                                
            dbc.Row([dbc.Col(html.Div([
                       html.Label(children='Max Heart Rate (bpm): '),
                       dcc.Input(
                           id='thalach',
                           type="number",
                           debounce=True,
                           value= 140.0
                       )]), 
                       width='auto')],style={'padding': '10px 10px'}),
                 
   html.Div("Stress test results",
                     style={'marginLeft': 30,
                            'font-weight': 'bold',
                            'font-weight': 'bold',
                            'font-color': 'black',
                            'font-size': 20}),
      
       dbc.Row([dbc.Col(html.Div([
               html.Label(children='Exercise induced angina:'),
               dcc.Dropdown(
                   options=[
                       {'label': 'No', 'value': 0.0},
                       {'label': 'Yes', 'value': 1.0}
                   ],
                   value= 0.0,
                   id='exang'
               )]), 
               width={'size': 3})],style={'padding': '10px 10px'}),
       dbc.Row([dbc.Col(html.Div([
               html.Label(children='ST depression: '),
               dcc.Input(
                   id='oldpeak',
                   type="number",
                   debounce=True,
                   value= 1.5
               )]), 
               width={'size': 3})],style={'padding': '10px 10px'}),
       dbc.Row([dbc.Col(html.Div([
               html.Label(children='ST slope: '),
               dcc.Dropdown(
                   options=[
                       {'label': 'Upsloping', 'value': 1.0},
                       {'label': 'Flat slope', 'value': 2.0},
                       {'label': 'Downsloping', 'value': 3.0}
                   ],
                   value= 3,
                   id='slope'
               )]),
               width={'size': 3})],style={'padding': '10px 10px'}),
         
        
   html.Div("Nuclear Medicine results",
                    style={'marginleft': 30,
                               'font-weight': 'bold',
                               'font-color': 'black',
                               'font-weight': 'bold',
                               'font-size': 20,
                               'textAlign': 'center'}),
       dbc.Row([dbc.Col(html.Div([
               html.Label(children='Affected vessels: '),
               dcc.Input(
                   id='ca',
                   type="number",
                   debounce=True,
                   value= 0.0
                  )]),
               width={'size': 3})],style={'padding': '10px 10px'}), 
       dbc.Row([dbc.Col(html.Div([
               html.Label(children='Thal Blood flow: '),
               dcc.Dropdown(
                   options=[
                       {'label': 'Normal', 'value': 3.0},
                       {'label': 'Fixed Defect', 'value': 6.0},
                       {'label': 'reversible Defect', 'value': 7.0},
                   ],
                   value= 3.0,
                   id='thal'
               )]),
               width={'size': 3})],style={'padding': '10px 10px'}),
                      
]),

@HDapp.callback(
    Output(component_id='patient_data',component_property="children"),
    [Input('age', 'value'),
     Input('sex', 'value'),
     Input('cp', 'value'),
     Input('trestbps', 'value'),
     Input('chol', 'value'),
     Input('fbs', 'value'),
     Input('restecg', 'value'),
     Input('thalach', 'value'),
     Input('exang', 'value'),
     Input('oldpeak', 'value'),
     Input('slope', 'value'),
     Input('ca', 'value'),
     Input('thal', 'value')]
)
def predict(age, sex,
            cp, trestbps,
            chol, fbs,
            restecg, thalach,
            exang, oldpeak,
            slope, ca, thal):

    df = pd.DataFrame(
        data=[[age, sex,
            cp, trestbps,
            chol, fbs,
            restecg, thalach,
            exang, oldpeak,
            slope, ca, thal]],
        columns=['age', 'sex',
            'cp', 'trestbps',
            'chol', 'fbs',
            'restecg', 'thalach',
            'exang', 'oldpeak',
            'slope', 'ca', 'thal'])
 
    prediction = model.predict(df)
    y_pred = model.predict_proba(df)[:, 1]*100
    text_pred = str(np.round(y_pred[0], 1)) + "%"
    
    # assign a risk group
    
    if y_pred/100 <= 0.275685: risk_grp = 'low risk'
    elif y_pred/100 <= 0.795583: risk_grp = 'medium risk'
    else: risk_grp = 'high risk'
    
    result = f"Based on the patient's profile, the predicted likelihood of developing heart disease is {prediction}, meaning a {text_pred} chance of developing CVD " \
           f"This patient is in the {risk_grp} group. "
    
    return result
