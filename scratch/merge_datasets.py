import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta

df_5k = pd.read_csv('datasets/5k.csv')
df_10k = pd.read_csv('datasets/10k.csv')
df_halfm = pd.read_csv('datasets/half_marathon.csv')

df_5k = df_5k[df_5k['chip_elapsed_time'].isnull() == False]
df_10k = df_10k[df_10k['chip_elapsed_time'].isnull() == False]
df_halfm = df_halfm[df_halfm['chip_elapsed_time'].isnull() == False]

def parseTime(t):
    """Normalize mix of H:MM:SS and MM:SS to HH:MM:SS"""
    time_string_split = t.split(":")
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
    td = timedelta(hours=hours,minutes=minutes,seconds=seconds)
    return str(td)

def convert_timedelta_to_minutes(row):
    time = row['chip_elapsed_time']
    time_split = time.split(":")
    hours = int(time_split[0])
    minutes = int(time_split[1])
    seconds = int(time_split[2])
    td = timedelta(hours=hours,minutes=minutes,seconds=seconds)
    return td.total_seconds()/60

df_5k['chip_elapsed_time'] = df_5k['chip_elapsed_time'].apply(parseTime)
df_10k['chip_elapsed_time'] = df_10k['chip_elapsed_time'].apply(parseTime)
df_halfm['chip_elapsed_time'] = df_halfm['chip_elapsed_time'].apply(parseTime)

df_5k['elapsed_time_minutes'] = df_5k.apply(convert_timedelta_to_minutes, axis=1)
df_10k['elapsed_time_minutes'] = df_10k.apply(convert_timedelta_to_minutes, axis=1)
df_halfm['elapsed_time_minutes'] = df_halfm.apply(convert_timedelta_to_minutes, axis=1)

df_5k = df_5k.assign(category="5k")
df_10k = df_10k.assign(category="10k")
df_halfm = df_halfm.assign(category="halfm")

df_merged = pd.concat([df_5k, df_10k, df_halfm])
df_merged['race_place'] = df_merged['race_place'].astype(dtype="int64") # for some reason the race place has float64 type after merging
print(df_merged)
df_merged.to_csv('datasets/merged_5k-10k-halfm.csv', index=False)

# df_merged.hist('elapsed_time_minutes', by='category')
# plt.show()