import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app, server
from apps import dashboard,noaccount



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='hello_user'),
    html.Div(id='page-content'),
])

login_page = html.Div([
    
    html.Div(style = {'background-color':'rgb(0,123,255)', 'width':'100%', 'height':40}),
    html.Div(dcc.Input(id="user", 
                       type="text", 
                       placeholder="Enter Username",
                       className="inputbox1",
                       style={'margin-left':'35%',
                              'width':'450px',
                              'height':'45px',
                              'padding':'10px',
                              'margin-top':'60px',
                              'font-size':'16px',
                              'border-width':'3px',
                              'border-color':'#a0a3a2'})),
    
    html.Div(dcc.Input(id="passw",
                       type="text",
                       placeholder="Enter Password",
                       className="inputbox2",
                       style={'margin-left':'35%',
                              'width':'450px',
                              'height':'45px',
                              'padding':'10px',
                              'margin-top':'10px',
                              'font-size':'16px',
                              'border-width':'3px',
                              'border-color':'#a0a3a2'})),
    
    html.Div(html.Button('Verify',
                         id='verify',
                         n_clicks=0,
                         style={'border-width':'3px',
                                'font-size':'14px'}),
             style={'margin-left':'45%',
                    'padding-top':'30px'}),
    
    html.Div(id='output1')
])


@app.callback(
    Output('url', 'pathname'),
    [Input('verify', 'n_clicks')],
    [State('user', 'value'),
     State('passw', 'value')])

def user_login(n_clicks, uname, passw):
    users={'cbagano':'password','jmmedina':'password'}
    if uname =='' or uname == None or passw =='' or passw == None:
        return '/'
    elif uname not in users:
        return '/unregistered'
    elif users[uname]==passw:
        return '/dashboard'
    else:
        return '/'
    

@app.callback(
    Output('hello_user', 'children'),
    [Input('verify', 'n_clicks')],
    [State('user', 'value')])

def welcome_User(n_clicks, uname):
    return[html.Div('Hello ' + uname)]

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return login_page
    elif pathname == '/dashboard':
        return dashboard.get_dashboard_layout()
    elif pathname == '/unregistered':
        return noaccount.no_account()
    else:
        return login_page

if __name__ == '__main__':
    app.run_server()
    
    
    
