import pandas as pd
import json

def create_stats_json_string_from_(file_object):
    df = pd.read_csv(file_object, delimiter=";")
    df['DateStamp'] = pd.to_datetime(df['DateStamp'])
    stats_dict = {}
    stats_dict["activity_distribution_per_incident"] = _create_activity_distribution_per_incident_stat(df)
    stats_dict["activity_distribution_over_days"] = _create_activity_dist_over_days(df)
    stats_dict["activity_distribution_over_hours"] = _create_activity_dist_over_hours(df)
    return stats_dict


def _create_activity_distribution_per_incident_stat(df):
    activity_distribution_per_incident = df.groupby(['Incident ID', 'IncidentActivity_Type']).size().reset_index(name='Count')
    return _convert_act_dist_df_into_groupped_json(activity_distribution_per_incident)


def _convert_act_dist_df_into_groupped_json(activity_distribution_per_incident):
    grouped_data = {}
    for _, row in activity_distribution_per_incident.iterrows():
        incident_id = row['Incident ID']
        activity_type = row['IncidentActivity_Type']
        count = row['Count']

        if incident_id not in grouped_data:
            grouped_data[incident_id] = []

        grouped_data[incident_id].append({
            'IncidentActivity_Type': activity_type,
            'Count': count
        })
    return [{'Incident ID': incident_id, 'Activities': activities} for incident_id, activities in grouped_data.items()]

def _create_activity_dist_over_days(df):
    df['Weekday'] = df['DateStamp'].dt.day_name()
    weekday_distribution = df.groupby('Weekday').size().reset_index(name='Count_per_Weekday')
    all_weekdays = pd.DataFrame({'Weekday': pd.date_range('2023-01-02', '2023-01-08').day_name()}) # trick to get Weekdays names
    weekday_distribution = all_weekdays.merge(weekday_distribution, on='Weekday', how='left').fillna(0)
    json_data = weekday_distribution.to_dict(orient='records')
    return json_data

def _create_activity_dist_over_hours(df):
    df['Hour'] = df['DateStamp'].dt.hour
    hourly_distribution = df.groupby('Hour').size().reset_index(name='Count_per_Hour')
    all_hours = pd.DataFrame({'Hour': range(24)})
    hourly_distribution = all_hours.merge(hourly_distribution, on='Hour', how='left').fillna(0)
    json_data = hourly_distribution.to_dict(orient='records')
    return json_data



if __name__ == "__main__":
    df = pd.read_csv("backend/data/Detail_Incident_Activity_small.csv", delimiter=";")
    df['DateStamp'] = pd.to_datetime(df['DateStamp'])
    print(_create_activity_dist_over_days(df))
    print(_create_activity_dist_over_hours(df))