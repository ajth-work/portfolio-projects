import sqlite3
import json

# Create or connect to the usage history database
conn_usage_history = sqlite3.connect('databases/usage_history.db')
cursor_usage_history = conn_usage_history.cursor()

# Create a table to store usage history
cursor_usage_history.execute('''
   CREATE TABLE IF NOT EXISTS usage_history (
    id INTEGER PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_type TEXT,
    source_id INTEGER,
    source_title TEXT,
    source_count INTEGER,
    source_method TEXT,
    original_query TEXT,
    query_count INTEGER,
    sentence_data JSON,
);

''')
conn_usage_history.commit()

# Construct sentence data for JSON objects
sentence_data = [
    {
        "sentence_id": 1,
        "sentence_text": "汪淼觉得...",
        "sentence_note": "...",  # Any additional notes for the sentence
        "translation": "Wang Miao felt...",
        "translation_note": "...",  # Any additional notes for the translation
        "vocab_analysis": {
            "learned_vocab_list": ["word1", "word2"],
            "learned_vocab_count": 2,
            "learned_vocab_percentage": 40,
            "not_learned_vocab_list": ["word3", "word4"],
            "not_learned_vocab_count": 2,
            "not_learned_vocab_percentage": 40,
            "unknown_vocab_list": ["word5"],
            "unknown_vocab_count": 1,
            "unknown_vocab_percentage": 20,
            "total_vocab_list": ["word1", "word2", "word3", "word4", "word5"],
            "total_vocab_count": 5,
            "avg_hsk_vocab_level": 3,  # Average HSK level of vocab
        },
        "char_analysis": {
            "learned_char_list": ["char1", "char2"],
            "learned_char_count": 2,
            "learned_char_percentage": 40,
            "not_learned_char_list": ["char3", "char4"],
            "not_learned_char_count": 2,
            "not_learned_char_percentage": 40,
            "unknown_char_list": ["char5"],
            "unknown_char_count": 1,
            "unknown_char_percentage": 20,
            "total_char_list": ["char1", "char2", "char3", "char4", "char5"],
            "avg_hsk_char_level": 4,  # Average HSK level of characters
        }
    },
]

# Convert sentence_data list to JSON format
sentence_data_json = json.dumps(sentence_data)

# Insert data into the usage_history table
insert_query = '''
    INSERT INTO usage_history (
        source_type,
        source_id,
        source_title,
        source_count,
        source_method,
        original_query,
        query_count,
        sentence_data
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
'''

cursor_usage_history.execute(
    insert_query,
    (source_type, source_id, source_title, source_count, source_method,
     original_query, query_count, sentence_data_json))

conn_usage_history.commit()
