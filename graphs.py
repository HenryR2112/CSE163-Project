import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set()

df_burke = pd.read_csv('Filtered Data\Ballard_filtered.csv')
df_elliot = pd.read_csv('Filtered Data\Elliot_filtered.csv')
df_burke = pd.read_csv('Filtered Data\Burke_filtered.csv')
df_fremont = pd.read_csv('Filtered Data\Fremont_filtered.csv')

sns.histplot(data=df_burke,x='Date', y='bike_sum', kde=True)
plt.xticks(rotation=-45)
plt.title('Burke Gilman Trail Bike Data')
plt.xlabel('Month and Year')
plt.ylabel('Bike Count')
plt.savefig('burke.png')
