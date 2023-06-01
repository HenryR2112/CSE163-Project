import plotly.graph_objects as go
import dash
from dash import Dash, dcc, html, dash_table
import pandas as pd

#import datasets and convert to datetime for easier manipulation
df_fremont = pd.read_csv('Filtered Data/fremont_filtered.csv')
df_ballard = pd.read_csv('Filtered Data/ballard_filtered.csv')
df_elliott = pd.read_csv('Filtered Data/elliot_filtered.csv')
df_burke = pd.read_csv('Filtered Data/burke_filtered.csv')
df_fremont['Date'] = pd.to_datetime(df_fremont['Date'])
df_ballard['Date'] = pd.to_datetime(df_ballard['Date'])
df_elliott['Date'] = pd.to_datetime(df_elliott['Date'])
df_burke['Date'] = pd.to_datetime(df_burke['Date'])

#set style guide
colors = {
    'background': '#3c434e',
    'text': '#f0f0f0'
}

#dash main method name
app = Dash(__name__)

figure = go.Figure()

#scaling factor selected to ensure that the diameter of the circles does
#not exceed the graph visually. Selected by trial and error.
SCALING_FACTOR = 0.12

# Add initial scatter plot points
for df, name in [(df_fremont, 'Fremont Bridge Sensor'), (df_ballard, 'NW 58th St Greenway at 22nd Ave NW Sensor'),
                 (df_elliott, 'Elliott-Bay Trail in Myrtle-Edwards Park Sensor'),
                 (df_burke, 'Burke-Gilman Trail NE 70th St Sensor')]:
    circle_marker = go.Scattermapbox(
        mode="markers",
        lon=df['lon'],
        lat=df['lat'],
        text=df['bike_sum'],
        marker=dict(
            size=df['bike_sum'] * SCALING_FACTOR,
            color=df['bike_sum'],
            opacity=0.04,
            colorscale=[[0, 'green']],
            sizemode='area'
        ),
        name=name
    )
    figure.add_trace(circle_marker)

#establishes custom made map styling using personal API access token and
#additional style elements.
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

#App HTML written using Dash syntax including the text and drawing of the graph,
# table, sliders, and additional elements.
app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1("Your App Title", style={'textAlign': 'center', 'color': colors['text'], 'fontFamily': 'Helvetica'}),
        html.P("Some flavor text above the map.", style={'color': colors['text'], 'fontFamily': 'Helvetica'}),
        dcc.Graph(
            id='map',
            figure=figure,
            style={'height': '70vh', 'margin': '0px'},
            config=dict(displayModeBar=False)
        ),
        html.P("Some flavor text below the map.", style={'color': colors['text'], 'fontFamily': 'Helvetica'}),
        html.Div([
            html.Label("Select Year:"),
            dcc.Slider(
                id='year-slider',
                min=df_fremont['Date'].dt.year.min(),
                max=df_fremont['Date'].dt.year.max(),
                value=df_fremont['Date'].dt.year.min(),
                marks={str(year): str(year) for year in range(df_fremont['Date'].dt.year.min(), df_fremont['Date'].dt.year.max()+1)},
                step=None
            )
        ], style={'width': '50%', 'margin': 'auto', 'marginTop': '10px', 'marginBottom': '10px'}),
        html.Div([
            html.Label("Select Month:"),
            dcc.Slider(
                id='month-slider',
                min=df_fremont['Date'].dt.month.min(),
                max=df_fremont['Date'].dt.month.max(),
                value=df_fremont['Date'].dt.month.min(),
                marks={str(month): str(month) for month in range(df_fremont['Date'].dt.month.min(), df_fremont['Date'].dt.month.max()+1)},
                step=None
            )
        ], style={'width': '50%', 'margin': 'auto'}),
        html.Div(id='table-container', style={'margin': 'auto', 'marginTop': '20px', 'width': 'fit-content'})
    ]
)

#callback decorator to provide functionality and interactivity to call between
#input and output of the server.
@app.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('year-slider', 'value'),
     dash.dependencies.Input('month-slider', 'value')]
)
def update_figure(year, month):
    '''
    update_figure is the function responsible for changing the graph display
    based on the input of the sliders. The inputs to the function are a year
    and month as dictated by the slider html elements and the result is an
    update to the interactive graph for the user. Inputs are restricted via
    the slider but reference a specific int year and int month.
    '''
    filtered_df_fremont = df_fremont[(df_fremont['Date'].dt.year == year) & (df_fremont['Date'].dt.month == month)]
    filtered_df_ballard = df_ballard[(df_ballard['Date'].dt.year == year) & (df_ballard['Date'].dt.month == month)]
    filtered_df_elliott = df_elliott[(df_elliott['Date'].dt.year == year) & (df_elliott['Date'].dt.month == month)]
    filtered_df_burke = df_burke[(df_burke['Date'].dt.year == year) & (df_burke['Date'].dt.month == month)]

    figure = go.Figure()

    # Update scatter plot points
    for df, name in [(filtered_df_fremont, 'Fremont Bridge Sensor'), (filtered_df_ballard, 'NW 58th St Greenway at 22nd Ave NW Sensor'),
                     (filtered_df_elliott, 'Elliott-Bay Trail in Myrtle-Edwards Park Sensor'),
                     (filtered_df_burke, 'Burke-Gilman Trail NE 70th St Sensor')]:
        circle_marker = go.Scattermapbox(
            mode="markers",
            lon=df['lon'],
            lat=df['lat'],
            text=df['bike_sum'],
            marker=dict(
                size=df['bike_sum'] * SCALING_FACTOR,
                color=df['bike_sum'],
                opacity=0.4,
                colorscale=[[0, 'green']],
                sizemode='area'
            ),
            name=name
        )
        figure.add_trace(circle_marker)

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

    return figure

#decorator to provide input output capabilites to table element
@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('year-slider', 'value'),
     dash.dependencies.Input('month-slider', 'value')]
)
def update_table(year, month):
    '''
    update_table is the function responsible for changing the table display
    based on the input of the sliders. The inputs to the function are a year
    and month as dictated by the slider html elements and the result is an
    update to the interactive table for the user. Inputs are restricted via
    the slider but reference a specific int year and int month.
    '''
    filtered_df_fremont = df_fremont[(df_fremont['Date'].dt.year == year) & (df_fremont['Date'].dt.month == month)]
    filtered_df_ballard = df_ballard[(df_ballard['Date'].dt.year == year) & (df_ballard['Date'].dt.month == month)]
    filtered_df_elliott = df_elliott[(df_elliott['Date'].dt.year == year) & (df_elliott['Date'].dt.month == month)]
    filtered_df_burke = df_burke[(df_burke['Date'].dt.year == year) & (df_burke['Date'].dt.month == month)]

    data = [
        {'Sensor': 'Fremont Bridge Sensor', 'Bike Sum': filtered_df_fremont['bike_sum'].sum()},
        {'Sensor': 'NW 58th St Greenway at 22nd Ave NW Sensor', 'Bike Sum': filtered_df_ballard['bike_sum'].sum()},
        {'Sensor': 'Elliott-Bay Trail in Myrtle-Edwards Park Sensor', 'Bike Sum': filtered_df_elliott['bike_sum'].sum()},
        {'Sensor': 'Burke-Gilman Trail NE 70th St Sensor', 'Bike Sum': filtered_df_burke['bike_sum'].sum()}
    ]

    columns = [{'name': 'Sensor', 'id': 'Sensor'}, {'name': 'Bike Sum', 'id': 'Bike Sum'}]

    return dash_table.DataTable(
        columns=columns,
        data=data,
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_cell={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white'
        },
    )


if __name__ == '__main__':
    app.run_server(debug=True)
