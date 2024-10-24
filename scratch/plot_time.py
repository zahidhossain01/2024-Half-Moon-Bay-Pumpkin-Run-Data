import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from datetime import timedelta

df = pd.read_csv('datasets/10k.csv')
df = df[df['chip_elapsed_time'].isnull() == False]
# print(df)

print()

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

df['chip_elapsed_time'] = df['chip_elapsed_time'].apply(parseTime)
df['elapsed_time_minutes'] = df.apply(convert_timedelta_to_minutes, axis=1)
print(df)
print()
print(df[df['bib_number'] == 428])
print(f"# of runners in M20 - 29 Group: {len(df[df['age_group'] == "M20 - 29"])}")

df.to_csv('testoutput.csv', index=False)

# df.hist('elapsed_time_minutes', bins=60, grid=False, density=True)
# plt.show()
