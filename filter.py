import pandas as pd

df_burke = pd.read_csv('Raw Data/Burke_Gilman_Trail_north_of_NE_70th_St_Bicycle_and_Pedestrian_Counter.csv', index_col='Date', parse_dates=True)
df_elliott = pd.read_csv('Raw Data/Elliott_Bay_Trail_in_Myrtle_Edwards_Park_Bicycle_and_Pedestrian_Counter.csv', index_col='Date', parse_dates=True)
df_fremont = pd.read_csv('Raw Data/Fremont_Bridge_Bicycle_Counter.csv', index_col='Date', parse_dates=True)
df_ballard = pd.read_csv('Raw Data/NW_58th_St_Greenway_at_22nd_Ave_NW_Bicycle_Counter.csv', index_col='Date', parse_dates=True)

START_DATE = pd.to_datetime('2018-01-01')
END_DATE = pd.to_datetime('2022-06-30')

df_burke.sort_index(inplace=True)
df_elliott.sort_index(inplace=True)
df_fremont.sort_index(inplace=True)
df_ballard.sort_index(inplace=True)

# Apply filtering
df_fremont_filtered = df_fremont.loc[START_DATE:END_DATE].copy()
df_burke_filtered = df_burke.loc[START_DATE:END_DATE].copy()
df_elliott_filtered = df_elliott.loc[START_DATE:END_DATE].copy()
df_ballard_filtered = df_ballard.loc[START_DATE:END_DATE].copy()

df_fremont_filtered['bike_sum'] = df_fremont_filtered['Fremont Bridge Sidewalks, south of N 34th St']
df_burke_filtered['bike_sum'] = df_burke_filtered['Bike North'] + df_burke_filtered['Bike South']
df_elliott_filtered['bike_sum'] = df_elliott_filtered['Bike North'] + df_elliott_filtered['Bike South']
df_ballard_filtered['bike_sum'] = df_ballard_filtered['NW 58th St Greenway st 22nd Ave NW Total']


df_fremont_filtered = df_fremont_filtered.resample('M').sum()
df_burke_filtered = df_burke_filtered.resample('M').sum()
df_elliott_filtered = df_elliott_filtered.resample('M').sum()
df_ballard_filtered = df_ballard_filtered.resample('M').sum()

df_fremont_filtered['lon'] = -122.349834
df_fremont_filtered['lat'] = 47.648116

df_burke_filtered['lon'] = -122.265128
df_burke_filtered['lat'] = 47.681344

df_elliott_filtered['lon'] = -122.356984
df_elliott_filtered['lat'] = 47.616238

df_ballard_filtered['lon'] = -122.384746
df_ballard_filtered['lat'] = 47.671213

df_fremont_filtered = df_fremont_filtered.loc[:, ['bike_sum', 'lon', 'lat']]
df_burke_filtered = df_burke_filtered.loc[:, ['bike_sum', 'lon', 'lat']]
df_elliott_filtered = df_elliott_filtered.loc[:, ['bike_sum', 'lon', 'lat']]
df_ballard_filtered = df_ballard_filtered.loc[:, ['bike_sum', 'lon', 'lat']]

df_fremont_filtered.to_csv('Filtered Data/fremont_filtered.csv')
df_burke_filtered.to_csv('Filtered Data/burke_filtered.csv')
df_elliott_filtered.to_csv('Filtered Data/elliot_filtered.csv')
df_ballard_filtered.to_csv('Filtered Data/ballard_filtered.csv')
