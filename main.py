import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('activity.csv')
df["date"] = pd.to_datetime(df['date'])
df['weekday'] = np.where(df['date'].dt.dayofweek < 5, 'weekday', 'weekend')

wd = df.groupby('weekday')
wd = wd.get_group('weekday')

we = df.groupby('weekday')
we = we.get_group('weekend')

wd[['interval', 'steps']].groupby('interval').mean().plot(kind='line', legend=None, title = "Weekday")
we[['interval', 'steps']].groupby('interval').mean().plot(kind='line', legend=None, title = "Weekend")