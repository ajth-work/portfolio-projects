import sqlite3


def analyze_duplicate_query(sentence):

    # Prepare historical database connections
    conn_history = sqlite3.connect('my_databases/historical_usage.db')
    cursor_history = conn_history.cursor()

    # Check if the sentence is in the historical database
    query = "SELECT * FROM sentences WHERE sentence = ?"
    cursor_history.execute(query, (sentence, ))
    result = cursor_history.fetchone()
    print(result)

    if result:
        # Sentence found in historical database, STATUS: Duplicate
        duplicate_info = {
            'translated_sentence': result[1],
            'analysis_data': result[2]
        }
        conn_history.close()
        return True, duplicate_info
    else:
        # Sentence not found in historical database, STATUS: Unique
        conn_history.close()
        return False, None
