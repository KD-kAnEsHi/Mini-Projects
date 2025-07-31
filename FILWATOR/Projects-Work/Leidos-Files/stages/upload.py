from dash import html, dcc, Output, Input, State
import pandas as pd
from shared.shared_data import shared_data
from shared.mock_data import mock_data

def layout():
    return html.Div([
        html.H2("Write code here for uploading file. For now, click Submit to use mock data."),
        dcc.Upload(id='upload-data', children=html.Button('Upload File')),
        html.Div(id='upload-feedback'),
        html.Button("Submit", id="submit-upload", n_clicks=0)
    ])

def register_callbacks(app):
    @app.callback(
        Output('upload-feedback', 'children'),
        Input('submit-upload', 'n_clicks'),
        State('upload-data', 'contents'),
    )
    def handle_submit_upload(n_clicks, contents):
        if n_clicks > 0:
            if contents:
                # Save mock DataFrame for demonstration
                shared_data["dataframes"] = mock_data["dataframes"]
                return "File uploaded and saved successfully!"
            
            # No upload, use mock data
            if not shared_data.get("dataframes"):
                shared_data["dataframes"] = mock_data["dataframes"]
            return "No file uploaded. Using mock data."

        return "Please upload a file or click Submit."
