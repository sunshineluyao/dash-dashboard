import os
from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# Sample data
df = pd.DataFrame({
    "Country": ["USA", "Canada", "Mexico"],
    "Cases": [1000, 500, 700]
})

# Dash App
app = Dash(__name__)

fig = px.bar(df, x="Country", y="Cases", title="Sample Dashboard")

app.layout = html.Div(children=[
    html.H1("COVID-19 Dashboard"),
    dcc.Graph(figure=fig)
])

# Main execution
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))  # Use environment variable PORT or default to 8050
    app.run_server(host="0.0.0.0", port=port)
