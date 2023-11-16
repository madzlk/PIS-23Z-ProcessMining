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
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    print("Rows fetched!")
    print(cursor.fetchall())
except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")

