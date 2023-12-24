import pytest
from backend.mongodb_connector.mongodb_conn import db, send_documents_to_db, send_incidents_to_db, put_csv_file_into_db
from backend.mongodb_connector.utils import fix_date_type_in_json


from bson.objectid import ObjectId


def are_docs_in_db(docs, ids, collection_name):
    for i, doc in enumerate(docs):
        doc["_id"] = ObjectId(ids[i])
        found = db[collection_name].find_one({'_id': ObjectId(ids[i])})
        if doc != found:
            return False
        
    return True



def test_send_documents_to_db_OneDocument():
    collection_name = "test1"
    collection = db[collection_name]
    _ = collection.delete_many({}) # Clear collection :) for testing

    
    documents = [{"name": "test1_document"}]
    result = send_documents_to_db(documents, collection_name)
    assert len(result.inserted_ids) == len(documents)

    found_documents = list(db[collection_name].find({"_id": {"$in": result.inserted_ids}}))
    assert found_documents


def test_send_documents_to_db_TwoDocuments():
    collection_name = "test2"
    collection = db[collection_name]
    _ = collection.delete_many({}) # Clear collection :) for testing

    documents = [{"name": "test2_document1"}, {"name": "test2_document2"}]
    result = send_documents_to_db(documents, collection_name)
    assert len(result.inserted_ids) == len(documents)

def test_send_incidents_to_db_One():
    username = "testuser"
    collection_name = f"incidents_{username}"

    collection = db[collection_name]
    _ = collection.delete_many({}) # Clear collection :) for testing

    incidents = [    {
        "Incident ID": "IM0000004",
        "DateStamp": "07-01-2013 08:17:17",
        "IncidentActivity_Number": "001A3689763",
        "IncidentActivity_Type": "Reassignment"
    }]
    result = send_incidents_to_db(incidents, username)
    ids = result.inserted_ids

    assert are_docs_in_db(incidents, ids, collection_name)

@pytest.fixture
def temp_csv_file1(tmp_path):
    content = """Incident ID;DateStamp;IncidentActivity_Number;IncidentActivity_Type;Assignment Group;KM number;Interaction ID\n
IM0000004;07-01-2013 08:17:17;001A3689763;Reassignment;TEAM0001;KM0000553;SD0000007\n
IM0000004;04-11-2013 13:41:30;001A5852941;Reassignment;TEAM0002;KM0000553;SD0000007\n
IM0000004;04-11-2013 13:41:30;001A5852943;Update from customer;TEAM0002;KM0000553;SD0000007\n
IM0000004;04-11-2013 12:09:37;001A5849980;Operator Update;TEAM0003;KM0000553;SD0000007\n
IM0000004;04-11-2013 12:09:37;001A5849979;Assignment;TEAM0003;KM0000553;SD0000007\n
IM0000004;04-11-2013 13:41:30;001A5852942;Assignment;TEAM0002;KM0000553;SD0000007\n
IM0000004;04-11-2013 13:51:18;001A5852172;Closed;TEAM0003;KM0000553;SD0000007\n
IM0000004;04-11-2013 13:51:18;001A5852173;Caused By CI;TEAM0003;KM0000553;SD0000007\n
IM0000004;04-11-2013 12:09:37;001A5849978;Reassignment;TEAM0003;KM0000553;SD0000007\n"""
    csv_file = tmp_path / 'test.csv'
    csv_file.write_text(content)
    return csv_file

def test_put_csv_into_db_larger(temp_csv_file1):
    username = "testuser"
    collection_name = f"incidents_{username}"

    collection = db[collection_name]
    _ = collection.delete_many({}) # Clear collection :) for testing

    expected_json = [
    {
        "Incident ID": "IM0000004",
        "DateStamp": "07-01-2013 08:17:17",
        "IncidentActivity_Number": "001A3689763",
        "IncidentActivity_Type": "Reassignment"
    },
    {
        "Incident ID": "IM0000004",
        "DateStamp": "04-11-2013 13:41:30",
        "IncidentActivity_Number": "001A5852941",
        "IncidentActivity_Type": "Reassignment"
    },
    {
        "Incident ID": "IM0000004",
        "DateStamp": "04-11-2013 13:41:30",
        "IncidentActivity_Number": "001A5852943",
        "IncidentActivity_Type": "Update from customer"
    },
    {
        "Incident ID": "IM0000004",
        "DateStamp": "04-11-2013 12:09:37",
        "IncidentActivity_Number": "001A5849980",
        "IncidentActivity_Type": "Operator Update"
    },
    {
        "Incident ID": "IM0000004",
        "DateStamp": "04-11-2013 12:09:37",
        "IncidentActivity_Number": "001A5849979",
        "IncidentActivity_Type": "Assignment"
    },
    {
        "Incident ID": "IM0000004",
        "DateStamp": "04-11-2013 13:41:30",
        "IncidentActivity_Number": "001A5852942",
        "IncidentActivity_Type": "Assignment"
    },
    {
        "Incident ID": "IM0000004",
        "DateStamp": "04-11-2013 13:51:18",
        "IncidentActivity_Number": "001A5852172",
        "IncidentActivity_Type": "Closed"
    },
    {
        "Incident ID": "IM0000004",
        "DateStamp": "04-11-2013 13:51:18",
        "IncidentActivity_Number": "001A5852173",
        "IncidentActivity_Type": "Caused By CI"
    },
    {
        "Incident ID": "IM0000004",
        "DateStamp": "04-11-2013 12:09:37",
        "IncidentActivity_Number": "001A5849978",
        "IncidentActivity_Type": "Reassignment"
    }
    ]
    fix_date_type_in_json(expected_json)
    result = put_csv_file_into_db(temp_csv_file1, username)
    ids = result.inserted_ids


    assert are_docs_in_db(expected_json, ids, collection_name)

def test_sanity_connector():
    assert True