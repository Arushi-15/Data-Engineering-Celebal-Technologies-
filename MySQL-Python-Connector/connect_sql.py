import mysql.connector

# Define connection settings
conn = mysql.connector.connect(
    host="localhost",        
    port=3306,
    user="root",
    password="Arushi@1508",    
    database="nyc_taxi"     
)

print("✅ MySQL connection successful!")

# Example query
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

cursor.close()
conn.close()


//OUTPUT:  mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'mysql-connector-python'
PS D:\Java basics> python -u "d:\Java basics\JavaBasic\connect_sql.py"
✅ MySQL connection successful!
PS D:\Java basics> python -u "d:\Java basics\JavaBasic\connect_sql.py"
✅ MySQL connection successful!
PS D:\Java basics> 
