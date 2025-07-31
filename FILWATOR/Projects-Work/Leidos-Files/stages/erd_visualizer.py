import dash
from dash import html, Input, Output, State
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

from shared.mock_data import mock_data
from shared.shared_data import shared_data

# Get mock data
shared_data["tables"] = mock_data["tables"]
shared_data["relationships"] = mock_data["relationships"]

tables, relationships = shared_data["tables"], shared_data["relationships"]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True

cyto_elements = []

# Set up spacing and initial positions for tables
horizontal_spacing = 300
vertical_height = 300
initial_positions = {table_name: 
                     (100 + i * horizontal_spacing, vertical_height)
                     for i, table_name in enumerate(tables)}

# Vertical spacing for columns
spacing = 50  

# Add table nodes and column nodes
for table_name, columns in tables.items():
    x, y = initial_positions[table_name]
    # Add table node
    cyto_elements.append({
        'data': {'id': table_name, 'label': table_name},
        'position': {'x': x, 'y': y},
        'classes': 'table'
    })

    # Add column nodes with dynamic positioning
    for i, column in enumerate(columns):
        col_id = f"{table_name}_{column}"
        cyto_elements.append({
            'data': {'id': col_id, 'label': column, 'parent': table_name},
            'position': {'x': x, 'y': y - (spacing * (i + 1))},
            'classes': 'column'
        })

# Add relationships
for (table1, table2, col1, col2) in relationships:
    col_id_1 = f"{table1}_{col1}"
    col_id_2 = f"{table2}_{col2}"
    cyto_elements.append({
        'data': {'source': col_id_1, 'target': col_id_2},
        'classes': 'relationship'
    })

# Layout
def layout():
    return html.Div([
    html.H2('ERD Visualizer with Mock Data:'),
    cyto.Cytoscape(
        id='cytoscape',
        elements=cyto_elements,
        style={'width': '100%', 'height': '700px'},
        layout={'name': 'preset'},
        stylesheet=[
            {
                'selector': 'node.table',
                'style': {
                    'shape': 'rectangle',
                    'background-color': '#B0C4DE',
                    'background-opacity': 0.7,
                    'border-width': '2px',
                    'border-color': '#4682B4',
                    'label': 'data(label)',
                    'width': '200px',
                    'height': 'auto',
                    'text-valign': 'top',
                    'text-halign': 'center',
                    'padding': '10px',
                }
            },
            {
                'selector': 'node.column',
                'style': {
                    'shape': 'rectangle',
                    'background-color': '#D3D3D3',
                    'background-opacity': 0.7,
                    'border-width': '1px',
                    'border-color': '#A9A9A9',
                    'label': 'data(label)',
                    'width': '180px',
                    'height': 'auto',
                    'text-valign': 'center',
                    'text-halign': 'center',
                    'font-size': '10px',
                    'padding': '5px',
                }
            },
            {
                'selector': 'node.column:active',
                'style': {
                    'background-color': '#C0C0C0',
                    'border-width': '1px',
                    'border-color': '#888888',
                }
            },
            {
                'selector': 'edge.relationship',
                'style': {
                    'width': 2,
                    'line-color': '#696969',
                    'target-arrow-color': '#696969',
                    'target-arrow-shape': 'triangle',
                    'z-index': 9999  # Ensure edges are on top
                }
            }
        ]
    ),
    dbc.Modal(
        [
            dbc.ModalHeader("Node Details"),
            dbc.ModalBody(id='modal-body'),
            dbc.ModalFooter(
                dbc.Button("Close", id="close-modal", className="ml-auto")
            ),
        ],
        id="modal",
        is_open=False,
    )
])

# Callbacks for interactivity
@app.callback(
    Output("modal", "is_open"),
    Output("modal-body", "children"),
    Input("cytoscape", "tapNode"),
    State("modal", "is_open"),
)
def display_node_info(node, is_open):
    if node:
        return not is_open, f"You clicked on {node['data']['label']}"
    return is_open, ""
