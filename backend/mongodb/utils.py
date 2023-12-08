import csv
import json
from datetime import datetime
import os

def csv_to_json(csv_file: str, json_file : str, columns_to_filter: list[str]):
    data = []
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            filtered_record = {key: value for key, value in row.items() if key not in columns_to_filter}
            data.append(filtered_record)

    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def _convert_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")

def fix_date_type_in_json(json_data):
    for record in json_data:
        if 'DateStamp' in record:
            record['DateStamp'] = _convert_date(record['DateStamp'])

def get_filename_without_ext(filename):
    base=os.path.basename(filename)
    return os.path.splitext(base)[0]


if __name__ == "__main__":
    csv_path = "backend/mongodb/data/Detail_Incident_Activity_small.csv"
    json_path = "backend/mongodb/data/Detail_Incident_Activity_small.json"
    columns_to_filter = ["Assignment Group","KM number","Interaction ID"]
    csv_to_json(csv_path, json_path, columns_to_filter)
