import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#READING THE FILE
df = pd.read_csv('activity.csv')
df["date"] = pd.to_datetime(df['date'])
df['weekday'] = np.where(df['date'].dt.dayofweek < 5, 'weekday', 'weekend')

wd = df.groupby('weekday')#GROUP THE TABLE INTO WEEKDAY
wd = wd.get_group('weekday')

we = df.groupby('weekday')#GROUP THE TABLE INTO WEEKEND
we = we.get_group('weekend')

#CREATING THE GRAPH
wd[['interval', 'steps']].groupby('interval').mean().plot(kind='line', legend=None, title = "Weekday")
we[['interval', 'steps']].groupby('interval').mean().plot(kind='line', legend=None, title = "Weekend")
