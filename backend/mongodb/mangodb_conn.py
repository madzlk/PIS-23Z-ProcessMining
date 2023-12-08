import pymongo
import json
from utils import fix_date_type_in_json, csv_to_json, get_filename_without_ext


mongo_host = "0.0.0.0"
mongo_port = 27017
mongo_db = "myapp_db"
mongo_collection = "incidents"
mongo_username = "root"  # Replace with your MongoDB username
mongo_password = "passwr"


columns_to_filter = ["Assignment Group","KM number","Interaction ID"]
client = pymongo.MongoClient(f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client[mongo_db]
collection = db[mongo_collection]

def put_csv_into_db(csv_path):
    json_path = get_filename_without_ext(csv_path) + ".json"
    csv_to_json(csv_path, json_path, columns_to_filter)
    with open(json_path, 'r') as file:
        json_data = json.load(file)
        fix_date_type_in_json(json_data)
        collection.insert_many(json_data)
    print("Data inserted successfully into MongoDB.")


if __name__ =="__main__":
    put_csv_into_db('/backend/mongodb/data/Detail_Incident_Activity_small.csv') # TODO