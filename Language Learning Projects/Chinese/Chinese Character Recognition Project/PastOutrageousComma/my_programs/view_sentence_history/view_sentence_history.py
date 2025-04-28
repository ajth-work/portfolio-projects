import sqlite3
from my_programs.imports.imports import linebreak


def view_sentence_history():

    # Set up sentence history connection and cursor
    conn_sentence = sqlite3.connect('my_databases/sentence_history.db')
    cursor_sentence = conn_sentence.cursor()

    # Create a table to store sentence history data if table doesn't already exist
    cursor_sentence.execute('''
    CREATE TABLE IF NOT EXISTS sentence_history (
    id INTEGER PRIMARY KEY,
    sentence TEXT NOT NULL,
    query_count INTEGER DEFAULT 0,
    sentence_translation TEXT,
    timestamp TIMESTAMP
    )
    ''')
    conn_sentence.commit()

    # Query all sentence records
    cursor_sentence.execute(
        "SELECT sentence, query_count, sentence_translation, timestamp FROM sentence_history"
    )
    sentence_records = cursor_sentence.fetchall()

    # Check if there are no sentence records
    if len(sentence_records) == 0:
        print("No sentence records found.")
    # If there are sentence records, print the information.
    else:
        print("Sentence History:")
        print(linebreak)
        for record in sentence_records:
            sentence, query_count, sentence_translation, timestamp = record
            print(f"Sentence: {sentence}")
            print(f"Query Count: {query_count}")
            print(f"Sentence Translation: {sentence_translation}")
            print(f"Last Query Timestamp: {timestamp}")
            print(linebreak)

    # Close the database connection
    conn_sentence.close()
