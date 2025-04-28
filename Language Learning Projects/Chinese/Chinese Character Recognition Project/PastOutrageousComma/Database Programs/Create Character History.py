import sqlite3
import datetime

# Connect to the character analysis database
conn_character = sqlite3.connect('my_databases/character_history.db')
cursor_character = conn_character.cursor()

# Create a table to store character analysis data
cursor_character.execute('''
   CREATE TABLE IF NOT EXISTS character_history (
    id INTEGER PRIMARY KEY,
    character TEXT NOT NULL,
    analysis_count INTEGER DEFAULT 0,
    character_info TEXT,
    timestamp TIMESTAMP
   )
''')
conn_character.commit()

# Example usage
# character_to_analyze = '好'
# character_info = 'Good character'
# insert_character_analysis(character_to_analyze, character_info)
