import mysql.connector
from log import Log


table_name = 'log'
db_config = {
    'host': '172.17.0.2',
    'user': 'user',
    'password': 'passwr',
    'database': 'db',
    }

def _map_rows_to_logs(rows):
    logs = []
    for row in rows:
        logs.append(Log(row[0],row[1],row[2], row[3]))
    return logs

def _map_logs_to_rows(logs:list[Log]):
    rows = []
    for log in logs:
        rows.append((log.log_id, log.incident_id, log.incident_activity_type, log.date_stamp))
    return rows

def get_logs_from_db():
    try:
        #connection = mysql.connector.connect(host='0.0.0.0', user='user',password='passwr',database='db') # działa gdy apka puszczona na hoscie a nie na containerze
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = f'SELECT * FROM {table_name}'
        cursor.execute(query)
        rows = cursor.fetchall()

    except mysql.connector.Error as e:
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

    return _map_rows_to_logs(rows)
    
def put_logs_into_db(logs):

    rows = _map_logs_to_rows(logs)
    insert_statements = []
    for row in rows:
        insert_statements.append(f"INSERT INTO {table_name} VALUES ({','.join(row)})") # Assumes each component of row is str.
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        for i_s in insert_statements:
            cursor.execute(i_s)
        connection.commit()
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
