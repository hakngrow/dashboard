import dash_html_components as html
import dash_table

import transforms

df = transforms.df

PAGE_SIZE = 50
#  html.Div([
#         dbc.Row([dbc.Col(html.Div(html.P("A single, half-width column")),style = {'padding':'50px'})
#                 ,dbc.Col(
layout = html.Div(
    dash_table.DataTable(
        id='table-sorting-filtering',
        columns=[
            {'name': i, 'id': i, 'deletable': True}
            for i in df[['country', 'description', 'points', 'price', 'province', 'title', 'variety', 'winery']]
        ],
        style_table={'height':'750px', 'overflowX': 'scroll', 'padding':'50px'},
        style_data_conditional=[{
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }],
        style_cell={
            'height': '90',
            # all three widths are needed
            'minWidth': '140px', 'width': '140px', 'maxWidth': '140px', 'textAlign': 'left', 'whiteSpace': 'normal'
        },
        style_cell_conditional=[
            {'if': {'column_id': 'description'}, 'width': '48%'},
            {'if': {'column_id': 'title'}, 'width': '18%'},
        ],
        page_current=0,
        page_size= PAGE_SIZE,
        page_action='custom',

        filter_action='custom',
        filter_query='',

        sort_action='custom',
        sort_mode='multi',
        sort_by=[]
    )
)
#             , width=9)
#     ])
# ])