import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set()

# load in the filtered data sets
df_ballard = pd.read_csv('Filtered Data\\Ballard_filtered.csv')
df_elliot = pd.read_csv('Filtered Data\\Elliot_filtered.csv')
df_burke = pd.read_csv('Filtered Data\\Burke_filtered.csv')
df_fremont = pd.read_csv('Filtered Data\\Fremont_filtered.csv')

df_burke['Date'] = pd.to_datetime(df_burke['Date'])
df_elliot['Date'] = pd.to_datetime(df_elliot['Date'])
df_ballard['Date'] = pd.to_datetime(df_ballard['Date'])
df_fremont['Date'] = pd.to_datetime(df_fremont['Date'])


# pre pandemic is January 1st, 2018 through December 31st, 2019
PRE_PANDEMIC_START = pd.to_datetime('2018-01-31')
PRE_PANDEMIC_END = pd.to_datetime('2019-12-31')

# pandemic is January 1st, 2020 through December 31st, 2021
PANDEMIC_START = pd.to_datetime('2020-01-31')
PANDEMIC_END = pd.to_datetime('2021-12-31')

# post pandemic is January 1st, 2022 through June 30th, 2022
POST_PANDEMIC_START = pd.to_datetime('2022-01-31')
POST_PANDEMIC_END = pd.to_datetime('2022-06-30')


def plot_pre_burke(df_burke: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_pre_burke = df_burke.loc[
        (df_burke['Date'] >= PRE_PANDEMIC_START) &
        (df_burke['Date'] <= PRE_PANDEMIC_END)
    ]
    sns.relplot(
        data=df_pre_burke, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Burke Gilman Trail Bike Data (Pre-Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Burke graphs\\pre_burke.png')


def plot_during_burke(df_burke: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_during_burke = df_burke.loc[
        (df_burke['Date'] >= PANDEMIC_START) &
        (df_burke['Date'] <= PANDEMIC_END)
    ]
    sns.relplot(
        data=df_during_burke, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Burke Gilman Trail Bike Data (Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Burke graphs\\pandemic_burke.png')


def plot_post_burke(df_burke: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_post_burke = df_burke.loc[
        (df_burke['Date'] >= POST_PANDEMIC_START) &
        (df_burke['Date'] <= POST_PANDEMIC_END)
    ]
    sns.relplot(
        data=df_post_burke, x='Date', y="bike_sum", kind='line',
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Burke Gilman Trail Bike Data (Post-Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Burke graphs\\post_burke.png')


def plot_pre_ballard(df_ballard: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_pre_ballard = df_ballard.loc[
        (df_ballard['Date'] >= PRE_PANDEMIC_START) &
        (df_burke['Date'] <= PRE_PANDEMIC_END)
    ]
    sns.relplot(
        data=df_pre_ballard, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Ballard Bike Data (Pre-Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Ballard graphs\\pre_ballard.png')


def plot_during_ballard(df_ballard: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_during_ballard = df_ballard.loc[
        (df_ballard['Date'] >= PANDEMIC_START) &
        (df_burke['Date'] <= PANDEMIC_END)
    ]
    sns.relplot(
        data=df_during_ballard, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Ballard Bike Data (Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Ballard graphs\\pandemic_ballard.png')


def plot_post_ballard(df_ballard: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_post_ballard = df_ballard.loc[
        (df_ballard['Date'] >= POST_PANDEMIC_START) &
        (df_burke['Date'] <= POST_PANDEMIC_END)
    ]
    sns.relplot(
        data=df_post_ballard, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Ballard Bike Data (Post-Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Ballard graphs\\post_ballard.png')


def plot_pre_elliot(df_elliot: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_pre_elliot = df_elliot.loc[
        (df_elliot['Date'] >= PRE_PANDEMIC_START) &
        (df_burke['Date'] <= PRE_PANDEMIC_END)
    ]
    sns.relplot(
        data=df_pre_elliot, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Elliot Bay Bike Data (Pre-Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Elliot graphs\\pre_elliot.png')


def plot_during_elliot(df_elliot: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_during_elliot = df_elliot.loc[
        (df_elliot['Date'] >= PANDEMIC_START) &
        (df_burke['Date'] <= PANDEMIC_END)
    ]
    sns.relplot(
        data=df_during_elliot, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Elliot Bay Bike Data (Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Elliot graphs\\pandemic_elliot.png')


def plot_post_elliot(df_elliot: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_post_elliot = df_elliot.loc[
        (df_elliot['Date'] >= POST_PANDEMIC_START) &
        (df_burke['Date'] <= POST_PANDEMIC_END)
    ]
    sns.relplot(
        data=df_post_elliot, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Elliot Bay Bike Data (Post-Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Elliot graphs\\post_elliot.png')


def plot_pre_fremont(df_fremont: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_pre_fremont = df_fremont.loc[
        (df_fremont['Date'] >= PRE_PANDEMIC_START) &
        (df_fremont['Date'] <= PRE_PANDEMIC_END)
    ]
    sns.relplot(
        data=df_pre_fremont, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Fremont Bridge Bike Data (Pre-Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Fremont graphs\\pre_fremont.png')


def plot_pandemic_fremont(df_fremont: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_during_fremont = df_fremont.loc[
        (df_fremont['Date'] >= PANDEMIC_START) &
        (df_fremont['Date'] <= PANDEMIC_END)
    ]
    sns.relplot(
        data=df_during_fremont, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Fremont Bridge Bike Data (Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Fremont graphs\\pandemic_fremont.png')


def plot_post_fremont(df_fremont: pd.DataFrame) -> None:
    '''
    comment
    '''
    df_post_fremont = df_fremont.loc[
        (df_fremont['Date'] >= POST_PANDEMIC_START) &
        (df_fremont['Date'] <= POST_PANDEMIC_END)
    ]
    sns.relplot(
        data=df_post_fremont, x="Date", y="bike_sum", kind="line",
        height=6, aspect=1.75
    )
    max_value = df_post_fremont['bike_sum'].max()
    print(max_value)
    plt.xticks(rotation=-30)
    plt.subplots_adjust(top=0.9, bottom=0.15)
    plt.title('Fremont Bridge Bike Data (Post-Pandemic)')
    plt.xlabel('Month and Year')
    plt.ylabel('Bike Count')
    plt.savefig('Fremont graphs\\post_fremont.png')


def main():
    plot_pre_burke()


if __name__ == "__main__":
    main()
