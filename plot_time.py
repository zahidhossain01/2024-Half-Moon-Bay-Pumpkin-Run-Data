import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta

df = pd.read_csv('10k.csv')
df = df[df['chip_elapsed_time'].isnull() == False]
# print(df)

print()

def convertTime(row):
    time_string_split = row['chip_elapsed_time'].split(":")
    hours = 0
    minutes = 0
    seconds = 0
    if(len(time_string_split) == 2):
        minutes = int(time_string_split[0])
        seconds = int(time_string_split[1])
    if(len(time_string_split) == 3):
        hours = int(time_string_split[0])
        minutes = int(time_string_split[1])
        seconds = int(time_string_split[2])
    return timedelta(hours=hours,minutes=minutes,seconds=seconds)

def convert_timedelta_to_minutes(row):
    td = row['elapsed_time_parsed']
    return td.total_seconds()/60

df['elapsed_time_parsed'] = df.apply(convertTime, axis=1)
df['elapsed_time_minutes'] = df.apply(convert_timedelta_to_minutes, axis=1)
print(df)
print()
print(df[df['bib_number'] == 428])


df.hist('elapsed_time_minutes', bins=30)
plt.show()
