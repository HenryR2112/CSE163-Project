import plotly.graph_objects as go
from dash import Dash, dcc, html
import pandas as pd

df = pd.read_csv('filtered_dataset.csv')
colors = {
    'background': '#3c434e',
    'text': '#f0f0f0'
}

app = Dash(__name__)

figure = go.Figure(
    go.Scattermapbox(
        mode="markers",
        lon=[-122.349834, -122.265128, -122.356984, -122.384746],
        lat=[47.648116, 47.681344, 47.616238, 47.671213],
        text=['Fremont Bridge Sensor',
              'Burke-Gilman Trail NE 70th St Sensor',
              'Elliott-Bay Trail in Myrtle-Edwards Park Sensor',
              'NW 58th St Greenway at 22nd Ave NW Sensor'],
        marker=dict(size=20)
    )
)
figure.update_layout(
    mapbox=dict(
        style='mapbox://styles/henryr2112/cli1742pb00sw01pzckx4a91l',
        accesstoken='pk.eyJ1IjoiaGVucnlyMjExMiIsImEiOiJjbGkxNnVkOXgwNnJuM21wanIzNWFtNGdjIn0.hFCNL4Sonao_UHwDoa6C5g',
        center=dict(lon=-122.333, lat=47.639),
        zoom=12,
        pitch=30
    ),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font={'color': colors['text']}
)

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1("Your App Title", style={'textAlign': 'center', 'color': colors['text'], 'fontFamily': 'Helvetica'}),
        html.P("Some flavor text above the map.", style={'color': colors['text'], 'fontFamily': 'Helvetica'}),
        dcc.Graph(
            id='map',
            figure=figure,
            style={'height': '80vh'},
            config=dict(displayModeBar=False)
        ),
        html.P("Some flavor text below the map.", style={'color': colors['text'], 'fontFamily': 'Helvetica'})
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
