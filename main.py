import plotly.graph_objects as go
from dash import Dash, dcc, html

app = Dash(__name__)

figure = go.Figure(
    go.Scattermapbox(
        mode="markers",
        lon=[-122.333],
        lat=[47.639]
    )
)
figure.update_layout(
    mapbox=dict(
        style='stamen-toner',
        center=dict(lon=-122.333, lat=47.639),
        zoom=11.5,
        pitch=30
    )
)

app.layout = html.Div([
    html.H1("Your App Title", style={'textAlign': 'center'}),
    html.P("Some flavor text above the map."),
    dcc.Graph(
        id='map',
        figure=figure,
        style={'height': '70vh'},
        config=dict(displayModeBar=False)
    ),
    html.P("Some flavor text below the map.")
])

if __name__ == '__main__':
    app.run_server(debug=True)
