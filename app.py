import dash_design_kit as ddk
from dash import Dash, html

app = Dash(__name__)
server = app.server  # expose server variable for Procfile

app.layout = html.Div(
    
    children=["An update"]
)

if __name__ == "__main__":
    app.run(debug=True)
