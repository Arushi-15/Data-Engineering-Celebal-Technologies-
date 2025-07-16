import mysql.connector

# Define MySQL connection settings
conn = mysql.connector.connect(
    host="localhost",        # or "127.0.0.1"
    port=3306,
    user="root",             # your MySQL username
    password="Arushi@1508",  # your actual password
    database="nyc_taxi"      # your database name
)

# Check connection
if conn.is_connected():
    print("✅ MySQL connection successful!")

    # Query the list of tables
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    for table in cursor.fetchall():
        print(table)

    cursor.close()
    conn.close()
else:
    print("❌ Failed to connect.")
