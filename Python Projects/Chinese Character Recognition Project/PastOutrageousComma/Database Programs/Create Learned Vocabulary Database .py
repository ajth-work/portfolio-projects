import sqlite3
import csv

# Connect to full vocabulary database
conn_learned_vocab = sqlite3.connect('learned_vocabulary_database.db')
cursor_learned_vocab = conn_learned_vocab.cursor()

# Create tables if they don't exist
cursor_learned_vocab.execute('''
    CREATE TABLE IF NOT EXISTS vocabulary (
        id INTEGER PRIMARY KEY,
        term TEXT,
        pinyin TEXT,
        definition TEXT,
        hsk_level INTEGER
    )
''')

# Commit changes and close the connection
conn_learned_vocab.commit()

# Read data from CSV and insert into the database
with open(
        'CSV Files/Chinese Character Recognition - Learned Vocabulary List.csv',
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
        cursor_learned_vocab.execute(
            '''
                INSERT INTO learned_vocabulary (
                    term, pinyin, definition, hsk_level
                ) 
                VALUES (?, ?, ?, ?)
            ''', fvl)

    conn_learned_vocab.commit()

# Query and print all rows
cursor_learned_vocab.execute('SELECT * FROM learned_vocabulary')
result = cursor_learned_vocab.fetchall()
for row in result:
    print(row)

conn_learned_vocab.close()
