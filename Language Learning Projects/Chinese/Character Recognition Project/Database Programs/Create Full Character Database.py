import sqlite3
import csv

conn = sqlite3.connect('full_character_database.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS full_characters (
        id INTEGER PRIMARY KEY,
        character TEXT,
        hanzidb_character_link TEXT,
        pinyin TEXT,
        tone INTEGER,
        definition TEXT,
        radical TEXT,
        hanzidb_radical_link TEXT,
        stroke_count INTEGER,
        hsk_level INTEGER,
        tgl INTEGER,
        tgl_number INTEGER,
        frequency_rank INTEGER,
        note TEXT,
        system_id INTEGER,
        length INTEGER,
        radical_order TEXT,
        general_standard TEXT
    )
''')
conn.commit()

# Read data from CSV and insert into the database
with open('Chinese Character Recognition - Full Characters.csv',
          'r',
          newline='',
          encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    for row in csvreader:
        ccr = (
            row[1],  # character
            row[2],  # hanzidb_character_link
            row[3],  # pinyin
            int(row[4]),  # tone
            row[5],  # definition
            row[6],  # radical
            row[7],  # hanzidb_radical_link
            row[8],  # stroke_count
            int(row[9]),  # hsk_level
            row[10],  # tgl
            int(row[11]),  # tgl_number
            row[12],  # frequency_rank
            row[13],  # note
            int(row[14]),  # system_id
            int(row[15]),  # length
            int(row[16]),  # radical_order
            int(row[17]),  # general_standard
        )
        cursor.execute(
            '''
                INSERT INTO full_characters (
                    character, hanzidb_character_link, pinyin, tone, definition, radical, hanzidb_radical_link,
                    stroke_count, hsk_level, tgl, tgl_number, frequency_rank, 
                    note, system_id, length, radical_order, general_standard
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', ccr)

    conn.commit()

# Query and print all rows
cursor.execute('SELECT * FROM full_characters')
result = cursor.fetchall()
for row in result:
    print(row)

conn.close()
