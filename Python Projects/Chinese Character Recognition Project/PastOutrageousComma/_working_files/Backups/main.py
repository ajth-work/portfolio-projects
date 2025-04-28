import sqlite3
import csv

# Connect to full vocabulary database
conn_full_vocab = sqlite3.connect('full_vocabulary_database.db')
cursor_full_vocab = conn_full_vocab.cursor()

# Create tables if they don't exist
cursor_full_vocab.execute('''
    CREATE TABLE IF NOT EXISTS vocabulary (
        id INTEGER PRIMARY KEY,
        term TEXT,
        pinyin TEXT,
        english TEXT,
        hsk_level INTEGER,
    )
''')

# Commit changes and close the connection
conn_full_vocab.commit()

# Read data from CSV and insert into the database
with open('Chinese Character Recognition - Full Vocabulary List.csv',
          'r',
          newline='',
          encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    for row in csvreader:
        fvl = (
            row[1],  # term
            row[2],  # pinyin
            row[3],  # definition
            int(row[4]),  # hsk_level
        )
        cursor_full_vocab.execute(
            '''
                INSERT INTO vocabulary (
                    term, pinyin, definition, hsk_level
                ) 
                VALUES (?, ?, ?, ?)
            ''', fvl)

    conn_full_vocab.commit()

# Query and print all rows
cursor_full_vocab.execute('SELECT * FROM vocabulary')
result = cursor_full_vocab.fetchall()
for row in result:
    print(row)

conn_full_vocab.close()
