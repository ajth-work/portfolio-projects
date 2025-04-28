import sqlite3

# Connect to historical usage database
conn_history = sqlite3.connect('historical_usage.db')
cursor_history = conn_history.cursor()

# Create tables if they don't exist
cursor_history.execute('''
    CREATE TABLE IF NOT EXISTS sentences (
        id INTEGER PRIMARY KEY,
        sentence TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
''')

# Commit changes and close the connection
conn_history.commit()
conn_history.close()

import sqlite3

# Connect to historical usage database
conn_history = sqlite3.connect('historical_usage.db')
cursor_history = conn_history.cursor()

# Create tables if they don't exist
cursor_history.execute('''
    CREATE TABLE IF NOT EXISTS sentences (
        id INTEGER PRIMARY KEY,
        sentence TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        searches INTEGER DEFAULT 0,
        first_search TEXT,
        most_recent_search TEXT,
        total_words_analyzed INTEGER,
        total_characters INTEGER,
        learned_characters INTEGER,
        not_learned_characters INTEGER,
        learned_words INTEGER,
        not_learned_words INTEGER,
        average_hsk_level REAL
    )
''')

# Commit changes and close the connection
conn_history.commit()
conn_history.close()
