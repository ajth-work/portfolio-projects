import sqlite3
import csv

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY,
        original TEXT,
        import_test TEXT,
        reading TEXT,
        tone INTEGER,
        definition TEXT,
        radical TEXT,
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
with open(
        'Chinese Character Recognition - Duolingo Level Analysis (Characters).csv',
        'r',
        newline='',
        encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    for row in csvreader:
        ccr = (
            row[0],  # id 
            row[1],  # original
            row[2],  # import_test
            row[3],  # reading
            int(row[4]),  # tone
            row[5],  # definition
            row[6],  # radical
            int(row[7]),  # stroke_count
            int(row[8]),  # hsk_level
            row[9],  # tgl
            int(row[10]),  # tgl_number
            int(row[11]),  # frequency_rank
            row[12],  # note
            int(row[13]),  # system_id
            int(row[14]),  # length
            int(row[15]),  #  radical_order
            int(row[16]),  # general_standard
        )
        cursor.execute(
            '''
                INSERT INTO characters (
                    id, original, import_test, reading, tone, definition, radical, 
                    stroke_count, hsk_level, tgl, tgl_number, frequency_rank, 
                    note, system_id, length, radical_order, general_standard
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', ccr)

    conn.commit()

# Query and print all rows
cursor.execute('SELECT * FROM characters')
result = cursor.fetchall()
for row in result:
    print(row)

conn.close()
