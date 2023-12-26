import pandas as pd
import json
import os

# Read the CSV file into a DataFrame
df = pd.read_csv("backend/data/Detail_Incident_Activity_small.csv", delimiter=";")

df['DateStamp'] = pd.to_datetime(df['DateStamp'])

# Extract hour and weekday
df['Hour'] = df['DateStamp'].dt.hour
df['Weekday'] = df['DateStamp'].dt.day_name()

# Distribution of events based on hours
hourly_distribution = df.groupby('Hour').size().reset_index(name='Count_per_Hour')

# Distribution of events per weekday
weekday_distribution = df.groupby('Weekday').size().reset_index(name='Count_per_Weekday')

# Create template for all hours (0-23) and all weekdays
all_hours = pd.DataFrame({'Hour': range(24)})
all_weekdays = pd.DataFrame({'Weekday': pd.date_range('2023-01-01', '2023-01-07').day_name()})

# Merge with distribution data to fill in missing hours and weekdays
hourly_distribution = all_hours.merge(hourly_distribution, on='Hour', how='left').fillna(0)
weekday_distribution = all_weekdays.merge(weekday_distribution, on='Weekday', how='left').fillna(0)

print(hourly_distribution)
print(weekday_distribution)

# Group by Incident ID and find the minimum and maximum DateStamp for each group
incident_times = df.groupby('Incident ID')['DateStamp'].agg(['min', 'max'])

print(incident_times)



