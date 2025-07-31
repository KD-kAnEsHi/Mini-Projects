from dash import Dash, html, dcc, Input, Output
from stages import upload, column_selection, erd_visualizer

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1("Welcome to Leidos!"),
    dcc.Tabs(id='tabs', value='upload', children=[
        dcc.Tab(label='Upload Files', value='upload'),
        dcc.Tab(label='Select Columns', value='columns'),
        dcc.Tab(label='ERD Visualizer', value='erd'),
    ]),
    html.Div(id='tab-content')
])

@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'value'),
)
def render_tab(tab):
    if tab == 'upload':
        return upload.layout()
    elif tab == 'columns':
        return column_selection.layout()
    elif tab == 'erd':
        return erd_visualizer.layout()

# Register callbacks for each stage
upload.register_callbacks(app)
column_selection.register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
