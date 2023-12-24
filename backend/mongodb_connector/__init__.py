import pymongo

mongo_host = "0.0.0.0"
mongo_port = 27017

mongo_db = "myapp_db"
mongo_username = "root"  # Replace with your MongoDB username
mongo_password = "passwr"

client = pymongo.MongoClient(f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client[mongo_db]