import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set()

# load in the filtered data sets
df_burke = pd.read_csv('Filtered Data\Ballard_filtered.csv')
df_elliot = pd.read_csv('Filtered Data\Elliot_filtered.csv')
df_burke = pd.read_csv('Filtered Data\Burke_filtered.csv')
df_fremont = pd.read_csv('Filtered Data\Fremont_filtered.csv')

df_burke['Date'] = pd.to_datetime(df_burke['Date'])

# pre pandemic is January 1st, 2018 through December 31st, 2019 
PRE_PANDEMIC_START = pd.to_datetime('2018-01-31')
PRE_PANDEMIC_END = pd.to_datetime('2019-12-31')

# pandemic is January 1st, 2020 through December 31st, 2021 
PANDEMIC_START = pd.to_datetime('2020-01-31')
PANDEMIC_END = pd.to_datetime('2021-12-31')

# post pandemic is January 1st, 2022 through June 30th, 2022
POST_PANDEMIC_START = pd.to_datetime('2022-01-31')
POST_PANDEMIC_END = pd.to_datetime('2022-06-30')

# burke plot pre pandemic
df_pre_burke = df_burke.loc[
    (df_burke['Date'] >= PRE_PANDEMIC_START) & (df_burke['Date'] <= PRE_PANDEMIC_END)
]
sns.relplot(
    data=df_pre_burke, x="Date", y="bike_sum", kind="line",
)
plt.xticks(rotation=-45)
plt.title('Burke Gilman Trail Bike Data (Pre-Pandemic)')
plt.xlabel('Month and Year')
plt.ylabel('Bike Count')
plt.savefig('pre_burke.png')

# burke plot during pandemic
df_during_burke = df_burke.loc[
    (df_burke['Date'] >= PANDEMIC_START) & (df_burke['Date'] <= PANDEMIC_END)
]
sns.relplot(
    data=df_during_burke, x="Date", y="bike_sum", kind="line",
)
plt.xticks(rotation=-45)
plt.title('Burke Gilman Trail Bike Data (Pandemic)')
plt.xlabel('Month and Year')
plt.ylabel('Bike Count')
plt.savefig('pandemic_burke.png')