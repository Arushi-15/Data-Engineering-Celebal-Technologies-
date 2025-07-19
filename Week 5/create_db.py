import sqlite3

conn = sqlite3.connect("source.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS employee (id INTEGER, name STRING, age INTEGER)")
cursor.executemany("INSERT INTO employee VALUES (?, ?, ?)", [
    (1, 'Arushi', 24), (2, 'Ravi', 26), (3, 'Sneha', 25)
])
conn.commit()
