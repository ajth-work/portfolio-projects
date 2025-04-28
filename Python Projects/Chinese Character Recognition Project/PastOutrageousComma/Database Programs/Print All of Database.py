import sqlite3
import csv

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

# Query and print all rows
cursor.execute('SELECT * FROM characters')
result = cursor.fetchall()
for row in result:
    print(row)

conn.close()
