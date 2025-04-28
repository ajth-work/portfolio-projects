import datetime
import sqlite3
import jieba
import string
import re
import html
import json

import sqlite3
import datetime

from my_programs.analyze.analyze_punctuation import punctuation_chars, alphabet_chars
from my_programs.analyze.analyze_hsk_char_level import calculate_average_hsk
from my_programs.analyze.database_connections import (
    conn1, conn2, conn3, conn4, conn_history, conn_usage_history, cursor1,
    cursor2, cursor3, cursor4, cursor_history, cursor_usage_history)
from my_programs.imports.imports import linebreak
from my_programs.analyze.analyze_get_char_details import get_char_details

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


def analyze_char(text):
    total_hsk_sum = 0
    non_punctuation_count = 0
    char_position = 1

    char_results_list = []

    for char in text:
        if char in punctuation_chars or alphabet_chars:
            continue
        char_results = get_char_details(char_position, char, total_hsk_sum,
                                        non_punctuation_count)
        char_results_list.append(char_results[2])
        char_position += 1
        total_hsk_sum += char_results[3]
        non_punctuation_count += char_results[4]

        # Insert or update character analysis data in the character_history.db database
        char_info = f"Additional information about character {char}"  # Replace with actual character info
        insert_character_analysis(char, char_info)

    for result in char_results_list:
        hsk_level = result['HSK Level']
        learned_status = result['Status']
        char = result['Character']
        pinyin = result['Pinyin']
        definition = result['Definition']

        if hsk_level == 0:
            hsk_text = 'Not in HSK'
        else:
            hsk_text = f'HSK {hsk_level}'

        if learned_status == 'Learned':
            learned_text = 'Learned'
        else:
            learned_text = 'Not Learned'

        print(
            f"{result['Position']} - {char} ({pinyin}) - {definition} - {hsk_text} - {learned_text}"
        )

    # get_char_details outputs: return char_position, char, char_details, total_hsk_sum, non_punctuation_count
    # Why is the following function producing "None"?
    calculate_average_hsk(total_hsk_sum, non_punctuation_count)
    return char_results_list


# Function to insert or update character analysis data
def insert_character_analysis(character, character_info):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = f"SELECT analysis_count FROM character_history WHERE character = '{character}'"
    cursor_character.execute(query)
    result = cursor_character.fetchone()

    if result:
        analysis_count = result[0]
        analysis_count += 1
        update_query = f"UPDATE character_history SET analysis_count = {analysis_count}, character_info = '{character_info}', timestamp = '{timestamp}' WHERE character = '{character}'"
        cursor_character.execute(update_query)
    else:
        insert_query = f"INSERT INTO character_history (character, analysis_count, character_info, timestamp) VALUES ('{character}', 1, '{character_info}', '{timestamp}')"
        cursor_character.execute(insert_query)

    conn_character.commit()
