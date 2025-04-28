import sqlite3


def view_historical_usage():
    # Connect to historical usage database
    conn_history = sqlite3.connect('databases/historical_usage.db')
    cursor_history = conn_history.cursor()

    # Query sentences and characters
    cursor_history.execute('SELECT * FROM sentences')
    sentences = cursor_history.fetchall()

    for sentence in sentences:
        sentence_id = sentence[0]
        sentence_text = sentence[1]
        timestamp = sentence[2]

        print(f"Sentence ID: {sentence_id}")
        print(f"Sentence: {sentence_text}")
        print(f"Timestamp: {timestamp}\n")

    # Avoid displaying duplicates
    # Go for first searched if searched multiple times and most recent search time
    # Show how many total words found,
    # how many learned words found, how many not learned words found, learned words / total words

    # percentage, average HSK level of vocab or characters.

    # Record/show if it was Vocabulary Analysis or Character Analysis or both

    # Close the connection
    conn_history.close()
    print("-------------------------\n")


pass
