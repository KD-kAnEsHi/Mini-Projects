from dash import html, dcc, Output, Input, State
from shared.shared_data import shared_data

def layout():
    return html.Div([
        html.H2("Write code here for selecting columns."),
        dcc.Dropdown(id='column-dropdown', multi=True),
        html.Div(id='column-feedback'),
        html.Button("Submit", id="submit-columns", n_clicks=0)
    ])

def register_callbacks(app):
    @app.callback(
        Output('column-dropdown', 'options'),
        Input('submit-columns', 'n_clicks'),
    )
    def update_columns(n_clicks):
        # Fetch columns from shared_data
        dataframes = shared_data["dataframes"]
        if dataframes:
            # For demonstration: get the first key (table name) and use its columns
            first_key = next(iter(dataframes))
            columns = [{"label": col, "value": col} for col in dataframes[first_key].columns]
            return columns
        return []

    @app.callback(
        Output('column-feedback', 'children'),
        Input('submit-columns', 'n_clicks'),
        State('column-dropdown', 'value'),
    )
    def handle_submit_columns(n_clicks, selected_columns):
        if n_clicks > 0:
            if selected_columns:
                shared_data["selected_columns"] = selected_columns
                return f"Selected columns saved: {', '.join(selected_columns)}"
            return "No columns selected."
        return "Please select columns and click Submit."
