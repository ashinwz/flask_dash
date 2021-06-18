import dash
import dash_html_components as html
import dash_core_components as dcc
from dash_flask_login import FlaskLoginAuth


def create_dash():
    app = dash.Dash(__name__, server=False, url_base_pathname='/dash/')

    #auth = FlaskLoginAuth(app)
    app.layout = html.Div([
        html.H1('Dash application'),
        dcc.Graph(
            id='basic-graph',
            figure={
                'data': [
                    {
                        'x': [0, 1],
                        'y': [0, 1],
                        'type': 'line'
                    }
                ],
                'layout': {
                    'title': 'Basic Graph'
                }
            }
        )
    ])
    return app
