import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

data = [['Blue',20],['Red ',12],['Green',33]]
df = pd.DataFrame(data,columns=['Color','Number'])

data1 = [['A',10,88],['B ',50,45],['C',25,120]]
df1 = pd.DataFrame(data1,columns=['Letter','Column1','Column2'])

app.layout = html.Div(children=[
    html.H1(children='Colors and Letters', style={'text-align': 'center'}),
    html.Div(children='Color', style={'text-align': 'center'}),

    html.Div([
        html.Label(['Choose a graph:'],style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'graph1', 'value': 'graph1'},
                {'label': 'graph2', 'value': 'graph2'},
                    ],
            value='graph1',
            style={"width": "60%"}),
        
    html.Div(dcc.Graph(id='graph')),        
        ]),

])

@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='dropdown', component_property='value')]
)
def select_graph(value):
    if value == 'graph1':
        fig = px.bar(df, x=df['Color'], y=df['Number'])
        return fig
    else:
        fig1 = px.line(x=df1['Letter'], y=df1['Column1'], color=px.Constant('Column1'),
                     labels=dict(x='Letter', y='Column1', color='Letter'))
        fig1.add_bar(x=df1['Letter'], y=df1['Column2'], name='Letter')
        return fig1
    
if __name__ == '__main__':
    app.run_server(debug=True)
