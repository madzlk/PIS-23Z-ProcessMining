import mysql.connector

db_config = {
    'host': '172.17.0.2',      # MySQL container name or host machine's IP address
    'user': 'user',
    'password': 'passwr',
    'database': 'db',
}
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    table_name = 'log'
    query = f"INSERT INTO {table_name} (incident_id) VALUES ('IMO80')"
    cursor.execute(query)
    connection.commit()
    print("Row inserted successfully!")
except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")

