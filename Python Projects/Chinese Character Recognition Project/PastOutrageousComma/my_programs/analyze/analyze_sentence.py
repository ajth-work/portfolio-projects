import sqlite3
import datetime


# Function to insert or update character analysis data
def insert_sentence(sentence, sentence_translation):
    conn_sentence = sqlite3.connect('my_databases/sentence_history.db')
    cursor_sentence = conn_sentence.cursor()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = f"SELECT query_count FROM sentence_history WHERE sentence = '{sentence}'"
    cursor_sentence.execute(query)
    result = cursor_sentence.fetchone()

    if result:
        query_count = result[0]
        query_count += 1
        update_query = f"UPDATE sentence_history SET query_count = {query_count}, sentence_translation = '{sentence_translation}', timestamp = '{timestamp}' WHERE sentence = '{sentence}'"
        cursor_sentence.execute(update_query)
    else:
        insert_query = f"INSERT INTO sentence_history (sentence, query_count, sentence_translation, timestamp) VALUES ('{sentence}', 1, '{sentence_translation}', '{timestamp}')"
        cursor_sentence.execute(insert_query)

    conn_sentence.commit()
