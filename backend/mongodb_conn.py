from pymongo import MongoClient

mongo_host = "0.0.0.0"
mongo_port = 27017
mongo_username = "root"
mongo_password = "passwr"
mongo_uri = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/"


client = MongoClient(mongo_uri)
mongo_db = "myapp_db"

def get_new_mongo_client():
    client = MongoClient(mongo_uri)
    return client

# valid_columns = ["Incident ID","DateStamp","IncidentActivity_Number","IncidentActivity_Type"]

# def send_incidents_to_db(incidents, username: str):
#     collection_name = f"incidents_{username}"
#     return send_documents_to_db(incidents, collection_name)

# def send_documents_to_db(documents: List, collection_name: str):
#     collection = db[collection_name]
#     return collection.insert_many(documents)


# def put_csv_file_into_db(csv_file, username: str):
#     incidents= csv_to_filtered_json(csv_file, valid_columns)
#     fix_date_type_in_json(incidents)
#     return send_incidents_to_db(incidents, username)




