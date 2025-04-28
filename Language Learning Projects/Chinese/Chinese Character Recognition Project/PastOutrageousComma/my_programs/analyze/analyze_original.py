import datetime
import sqlite3
import string
import re
import html
import json
import jieba
from my_programs.analyze.analyze_data_insertion import analyze_data_insertion

from my_programs.analyze.analyze_sentence_list import analyze_sentence_list
from my_programs.analyze.analyze_jieba import analyze_jieba
from my_programs.analyze.analyze_punctuation import punctuation_chars
from my_programs.analyze.analyze_translate import analyze_translate
from my_programs.analyze.analyze_vocab import analyze_vocab
from my_programs.analyze.analyze_char import analyze_char
from my_programs.imports.imports import linebreak
from my_programs.analyze.analyze_duplicate_query import analyze_duplicate_query


def analyze_original(text):
    sentence = None
    #Set up connections
    conn_history = sqlite3.connect('my_databases/historical_usage.db')
    # NEW - 09/14/2023 - conn_usage_history = sqlite3.connect('my_databases/usage_history.db')

    # Set up cursors
    cursor_history = conn_history.cursor()
    # NEW - 09/14/2023 - cursor_usage_history = conn_usage_history.cursor()

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

    # Itemize sentences
    sentences = analyze_sentence_list(text)

    # Display the count of sentences before analysis
    print(f"{len(sentences)} sentences discovered:\n")

    # List the sentences before analysis
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence.strip()}\n")
    # Sentence by Sentence Duplicate Check and Translation
    for i, sentence in enumerate(sentences, start=1):
        translation = None  # Initialize the translation variable

        # Check if the sentence already exists in the database
        query = "SELECT id, sentence_translation FROM sentence_history WHERE sentence = ?"
        cursor_sentence.execute(query, (sentence, ))
        result = cursor_sentence.fetchone()

        if result:
            # Sentence already exists, update query_count and timestamp
            sentence_id, translation = result
            update_query = "UPDATE sentence_history SET query_count = query_count + 1, timestamp = ? WHERE id = ?"
            cursor_sentence.execute(update_query,
                                    (datetime.datetime.now(), sentence_id))
            # Commit changes
            conn_sentence.commit()

        else:

            # Sentence is new, insert it into the database
            insert_query = "INSERT INTO sentence_history (sentence, timestamp) VALUES (?, ?)"
            cursor_sentence.execute(insert_query,
                                    (sentence, datetime.datetime.now()))

            # Prepare translation and save it to the new sentence's entry
            translation = analyze_translate(sentence)

            # Fetch the newly assigned sentence_id after insertion
            cursor_sentence.execute(query, (sentence, ))
            result = cursor_sentence.fetchone()
            if result:
                sentence_id = result[0]
                update_translation_query = "UPDATE sentence_history SET sentence_translation = ? WHERE id = ?"
                cursor_sentence.execute(update_translation_query,
                                        (translation, sentence_id))
                # Commit changes
                conn_sentence.commit()

        # Print the imported Chinese sentence
        print(linebreak)
        print(f"Target Sentence {i}")
        print(f"Sentence: [{sentence.strip()}]")
        print(f"Translated: [{translation}]")
        print(linebreak)

        # Ask for Vocabulary Analysis or Character Analysis or both
        analysis_choices = [
            "Vocabulary Analysis (Testing New Feature)", "Character Analysis",
            "Both"
        ]
        print("Choose analysis type:\n")
        for i, choice in enumerate(analysis_choices, start=1):
            print(f"{i}. {choice}\n")
        user_analysis_choice = input("Enter your choice: ")
        print(linebreak)

        if user_analysis_choice == '1':  # vocab analysis
            # analyze_vocab(sentence)
            analyze_data_insertion(sentence)
        elif user_analysis_choice == '2':  # char analysis
            analyze_char(sentence)
        elif user_analysis_choice == '3':  # both
            analyze_vocab(sentence)
            analyze_char(sentence)
        else:
            print("Invalid choice.")

        # Insert a record into the old historical usage database
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_query = f"INSERT INTO sentences (sentence, timestamp) VALUES ('{text}', '{timestamp}')"
        cursor_history.execute(insert_query)
        conn_history.commit()

    # Close the database connections
    conn_sentence.close()
    conn_history.close()

    # Offer options
    print(linebreak)
    print("What would you like to do next?\n")
    print("1. Return to the main menu\n")
    print("2. Analyze another sentence\n")
    user_choice = input("Enter your choice: ")

    print(linebreak)
    if user_choice == "1":
        return  # Return to the main menu
    elif user_choice == "2":
        user_sentence = input("Enter the new sentence for analysis: ")
        analyze_original(user_sentence)  # Analyze another sentence
    else:
        print("Invalid choice. Returning to the main menu.")
