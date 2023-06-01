'''
CSE163 Final Project Group 3
Henry Ramstad, Ani Ramadurai, Annika Halvorson

main.py is responsible for generating the UI and interactive
plots in the webpage as well as the embed PDF of the report. The
general strucuture of the app includes update functions for the slider
elements as well as app.layout which is a special variable which contains
pseudo-HTML and CSS for the styling and layout. Callback decorators are used
to provide interaction between the UI and Server side information and the main
method pattern follows the standard special to dash applications. Certain lines
in this file fail the flake8 line standard due to the syntax of Dash. 
'''
import plotly.graph_objects as go
import dash
from dash import Dash, dcc, html, dash_table
import pandas as pd
import flask

# import datasets and convert to datetime for easier manipulation
df_fremont = pd.read_csv('Filtered Data/fremont_filtered.csv')
df_ballard = pd.read_csv('Filtered Data/ballard_filtered.csv')
df_elliott = pd.read_csv('Filtered Data/elliot_filtered.csv')
df_burke = pd.read_csv('Filtered Data/burke_filtered.csv')
df_fremont['Date'] = pd.to_datetime(df_fremont['Date'])
df_ballard['Date'] = pd.to_datetime(df_ballard['Date'])
df_elliott['Date'] = pd.to_datetime(df_elliott['Date'])
df_burke['Date'] = pd.to_datetime(df_burke['Date'])

# set style guide
colors = {
    'background': '#3c434e',
    'text': '#f0f0f0'
}

# dash main method name
app = Dash(__name__)

figure = go.Figure()

# scaling factor selected to ensure that the diameter of the circles does
# not exceed the graph visually. Selected by trial and error.
SCALING_FACTOR = 0.12

# Add initial scatter plot points
for df, name in [(df_fremont,
                  'Fremont Bridge Sensor'),
                 (df_ballard,
                  'NW 58th St Greenway at 22nd Ave NW Sensor'),
                 (df_elliott,
                  'Elliott-Bay Trail in Myrtle-Edwards Park Sensor'),
                 (df_burke,
                  'Burke-Gilman Trail NE 70th St Sensor')]:
    circle_marker = go.Scattermapbox(
        mode="markers",
        lon=df['lon'],
        lat=df['lat'],
        text=df['bike_sum'],
        marker=dict(
            size=df['bike_sum'] * SCALING_FACTOR,
            color=df['bike_sum'],
            opacity=0.64,
            colorscale=[[0, 'green']],
            sizemode='area'
        ),
        name=name
    )
    figure.add_trace(circle_marker)

# establishes custom made map styling using personal API access token and
# additional style elements.
figure.update_layout(
    mapbox=dict(
        style='mapbox://styles/henryr2112/cli1742pb00sw01pzckx4a91l',
        accesstoken='pk.eyJ1IjoiaGVucnlyMjExMiIsImEiOiJjbGkxNnVkOXgwNnJuM21wanIzNWFtNGdjIn0.hFCNL4Sonao_UHwDoa6C5g',
        center=dict(lon=-122.333, lat=47.639),
        zoom=9,
        pitch=30
    ),
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font={'color': colors['text']}
)


@app.server.route("/pdf")
def serve_pdf():
    return flask.send_file("CSE_163_Project_Report.pdf",
                           attachment_filename="CSE_163_Project_Report.pdf")


# App HTML written using Dash syntax including the text and drawing of the
# graph,table, sliders, and additional elements.
app.layout = html.Div(
    style={'backgroundColor': colors['background'], 'padding': '20px'},
    children=[
        html.H1(
            "Understanding COVID-19's Effect on Bicycle Route Usage in Seattle from 2018 to 2022",
            style={'textAlign': 'center', 'color': colors['text'],
                   'fontFamily': 'Helvetica', 'border': '1px solid #ddd',
                   'padding': '10px', 'border-radius': '15px'}),
        html.P(
            "The map below displays interactive visuals of our data across 4 Seattle area bike sensors",
            style={'color': colors['text'], 'fontFamily': 'Helvetica',
                   'padding': '2px', 'margin': '10px'}),
        dcc.Graph(
            id='map',
            figure=figure,
            style={'height': '70vh', 'margin': '0px'},
            config=dict(displayModeBar=False)
        ),
        html.P(
            "Use the Sliders below to filter the data to specific months and years!",
            style={'color': colors['text'], 'fontFamily': 'Helvetica',
                   'padding': '10px', 'margin': '10px',
                   'textAlign': 'center'}),
        html.Div([
            html.Label("Select Year:", style={'color': colors['text'],
                                              'fontFamily': 'Helvetica'}),
            dcc.Slider(
                id='year-slider',
                min=df_fremont['Date'].dt.year.min(),
                max=df_fremont['Date'].dt.year.max(),
                value=df_fremont['Date'].dt.year.min(),
                marks={
                    str(year): str(year) for year in range(
                        df_fremont['Date'].dt.year.min(),
                        df_fremont['Date'].dt.year.max()+1)},
                step=None,
            )
        ], style={'width': '50%', 'margin': 'auto',
                  'marginTop': '10px', 'marginBottom': '10px',
                  'border': '1px solid #ddd', 'border-radius': '15px',
                  'padding': '7px'}),
        html.Div([
            html.Label("Select Month:", style={'color': colors['text'],
                                               'fontFamily': 'Helvetica'}),
            dcc.Slider(
                id='month-slider',
                min=df_fremont['Date'].dt.month.min(),
                max=df_fremont['Date'].dt.month.max(),
                value=df_fremont['Date'].dt.month.min(),
                marks={
                    str(month): str(month) for month in range(
                        df_fremont['Date'].dt.month.min(),
                        df_fremont['Date'].dt.month.max()+1)},
                step=None,
            )
        ], style={'width': '50%', 'margin': 'auto', 'border': '1px solid #ddd',
                  'padding': '10px', 'marginTop': '10px', 'marginBottom':
                  '10px', 'border-radius': '15px'}),
        html.H1('Data Table', style={'textAlign': 'center',
                                     'color': colors['text'],
                                     'fontFamily': 'Helvetica',
                                     'marginTop': '10px',
                                     'padding': '10px'}),
        html.Div(id='table-container', style={'margin': 'auto',
                                              'marginTop': '20px',
                                              'width': 'fit-content',
                                              'border': '1px solid #ddd',
                                              'padding': '10px',
                                              'border-radius': '15px',
                                              'marginBottom': '50px'}),
        html.H1('Report', style={'textAlign': 'center',
                                 'color': colors['text'],
                                 'fontFamily': 'Helvetica',
                                 'marginTop': '10px',
                                 'padding': '10px'}),
        html.Div(
            style={'width': '80%', 'margin': 'auto',
                   'marginTop': '10px', 'marginBottom': '90px',
                   'border': '6px solid #3c434e', 'border-radius': '15px'},
            children=[dash.html.Iframe(src="/pdf",
                                       style={'width': '100%',
                                              'height': '900px',
                                              'textAlign': 'center',
                                              'border': '1px solid #ddd',
                                              'padding': '10px',
                                              'border-radius': '15px'})]
        )
    ]
)


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
    filtered_df_fremont = df_fremont[
        (df_fremont['Date'].dt.year == year) &
        (df_fremont['Date'].dt.month == month)]
    filtered_df_ballard = df_ballard[
        (df_ballard['Date'].dt.year == year) &
        (df_ballard['Date'].dt.month == month)]
    filtered_df_elliott = df_elliott[
        (df_elliott['Date'].dt.year == year) &
        (df_elliott['Date'].dt.month == month)]
    filtered_df_burke = df_burke[
        (df_burke['Date'].dt.year == year) &
        (df_burke['Date'].dt.month == month)]

    figure = go.Figure()

    # Update scatter plot points
    for df, name in [
        (filtered_df_fremont,
         'Fremont Bridge Sensor'),
        (filtered_df_ballard,
         'NW 58th St Greenway at 22nd Ave NW Sensor'),
        (filtered_df_elliott,
         'Elliott-Bay Trail in Myrtle-Edwards Park Sensor'),
        (filtered_df_burke,
         'Burke-Gilman Trail NE 70th St Sensor')
            ]:
        circle_marker = go.Scattermapbox(
            mode="markers",
            lon=df['lon'],
            lat=df['lat'],
            text=df['bike_sum'],
            marker=dict(
                size=df['bike_sum'] * SCALING_FACTOR,
                opacity=0.64,
                colorscale=[[0, 'green']],
                sizemode='area'
            ),
            name=name
        )
        figure.add_trace(circle_marker)

    # Update layout
    figure.update_layout(
        mapbox=dict(
            style='mapbox://styles/henryr2112/cli1742pb00sw01pzckx4a91l',
            accesstoken='pk.eyJ1IjoiaGVucnlyMjExMiIsImEiOiJjbGkxNnVkOXgwNnJuM21wanIzNWFtNGdjIn0.hFCNL4Sonao_UHwDoa6C5g',
            center=dict(lon=-122.333, lat=47.639),
            zoom=11,
            pitch=30
        ),
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font={'color': colors['text']}
    )

    return figure


@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('year-slider', 'value'),
     dash.dependencies.Input('month-slider', 'value')]
)
def update_table(year, month):
    '''
    update_table is the function responsible for updating the data table
    displayed below the map based on the input of the sliders. The inputs to
    the function are a year and month as dictated by the slider html elements
    and the result is an update to the interactive table for the user.
    Inputs are restricted via the slider but reference a specific
    int year and int month.
    '''
    filtered_df_fremont = df_fremont[
        (df_fremont['Date'].dt.year == year) &
        (df_fremont['Date'].dt.month == month)]
    filtered_df_ballard = df_ballard[
        (df_ballard['Date'].dt.year == year) &
        (df_ballard['Date'].dt.month == month)]
    filtered_df_elliott = df_elliott[
        (df_elliott['Date'].dt.year == year) &
        (df_elliott['Date'].dt.month == month)]
    filtered_df_burke = df_burke[
        (df_burke['Date'].dt.year == year) &
        (df_burke['Date'].dt.month == month)]

    # Concatenate filtered dataframes into a single dataframe
    concatenated_df = pd.concat(
        [filtered_df_fremont, filtered_df_ballard,
         filtered_df_elliott, filtered_df_burke])

    # Create a datatable from the concatenated dataframe
    table = dash_table.DataTable(
        data=concatenated_df.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in concatenated_df.columns],
        style_table={'maxHeight': '300px', 'overflowY': 'scroll'},
        style_cell={'textAlign': 'left',
                    'backgroundColor': colors['background'],
                    'color': colors['text'], 'fontFamily': 'Helvetica'},
        style_header={'backgroundColor': colors['background'],
                      'color': colors['text'], 'fontFamily': 'Helvetica'}
    )

    return table


if __name__ == '__main__':
    app.run_server(debug=True)
