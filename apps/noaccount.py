import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import numpy as np
import sqlite3
from dash.exceptions import PreventUpdate
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

from app import app


# Add dashboard specific methods here

def no_account():

    # Call dashboard specific methods here

    return [
        html.Div(style = {'background-color':'rgb(0,123,255)', 'width':'100%', 'height':40}),
        html.Div('Unregistered User',style = {'color':'rgb(0,123,255)', 'font':'Verdana','font-size':40,}),
        html.Div('Register Here:',style = {'margin-left':'35%',
                                           'margin-top':'60px',
                                           'font-size':'20px',}),
        html.Div(dcc.Input(id="reguser", 
                           type="text", 
                           placeholder="Register Username",
                           style={'margin-left':'35%',
                                  'width':'450px',
                                  'height':'45px',
                                  'padding':'10px',
                                  'margin-top':'60px',
                                  'font-size':'16px',
                                  'border-width':'3px',
                                  'border-color':'#a0a3a2'})),
        
        html.Div(dcc.Input(id="regpassw",
                           type="text",
                           placeholder="Register Password",
                           style={'margin-left':'35%',
                                  'width':'450px',
                                  'height':'45px',
                                  'padding':'10px',
                                  'margin-top':'10px',
                                  'font-size':'16px',
                                  'border-width':'3px',
                                  'border-color':'#a0a3a2'})),
        
        html.Div(dcc.Link('Register', 
                          href='/dashboard',
                          style = {'fontSize': '20px',
                                   'color':'white',
                                   'background-color':'rgb(0,123,255)',
                                   'float':'middle',
                                   'border-radius':'5px',
                                   'border':'5px'}))

    
    ]
    
    

        
        
    