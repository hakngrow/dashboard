import dash_html_components as html
import dash_core_components as dcc

import transforms

df = transforms.df

layout = html.Div([

     html.Div(
         [html.H3("Visualize:")],
         style={'textAlign': "Left"}
     ),

    html.Div([
        dcc.Dropdown(
            id="selected-feature",
            options=[{"label": i, "value": i} for i in ['price','rating']],
            value='price',
            style={"display": "block", "width": "80%"}
        )
    ]),

    html.Div([
        dcc.Graph(
            id="ru-my-heatmap",
            style={"margin-right": "auto", "margin-left": "auto", "width": "80%", "height":"700px"}
        )
    ])
])


def update_figure(country, province, feature, variety):

    return {
        "data": [trace],
        "layout": {
            "xaxis": {"automargin": False},
            "yaxis": {"automargin": True, 'side': "right"},
            "margin": {"t": 10, "l": 30, "r": 100, "b":230}
        }
    }
