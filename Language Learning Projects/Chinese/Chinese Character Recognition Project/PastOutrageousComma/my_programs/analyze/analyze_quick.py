import datetime
import sqlite3
import jieba
import string
import re
import html
import json

# Google Translation Services
import os

# Get the value of the environment variable
google_application_credentials = os.environ.get(
    "GOOGLE_APPLICATION_CREDENTIALS")

from google.cloud import translate_v2 as translate

client = translate.Client()


# Function to translate text using Google Translate
def translate_text(text, target_language):
    result = client.translate(text, target_language=target_language)
    return result['translatedText']


jieba.setLogLevel(20)


def capture_and_analyze(text):
    conn1 = sqlite3.connect('databases/learned_character_database.db')
    conn2 = sqlite3.connect('databases/full_character_database.db')
    conn3 = sqlite3.connect('databases/learned_vocabulary_database.db')
    conn4 = sqlite3.connect('databases/full_vocabulary_database.db')
    conn_history = sqlite3.connect('databases/historical_usage.db')
    conn_usage_history = sqlite3.connect('databases/usage_history.db')

    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()
    cursor3 = conn3.cursor()
    cursor4 = conn4.cursor()
    cursor_history = conn_history.cursor()
    cursor_usage_history = conn_usage_history.cursor()

    # Direct the user towards data entry for new content or streamlined access to previously categorized content
    entry_type = input("""
        1. New Source (starting a new collection)\n
        2. Old Source (adding to a previous collection)\n
        """)
    if entry_type == 1:
        source_type = input("""
        What type of source?
        1. Book
        2. Internet
        3. User
        """)
        if source_type == 1:
            source_title = input("Enter the name of book: ") 
        elif source_type == 2:
            source_link = input("Enter the link from the internet: ")
        elif source_type == 3:
            source_note = input("Enter note from user: ")

    elif entry_type == 2: 
        # make a call to the existing source types section of the database
        #list what source types there are currently 
        # for source_type in source_types, print source_type
            # source in source_type, print source

    
    
    # Define the major data points for the query
        source_id = ""# database-defined

    source_link = input("Enter source link if from internet: ")
    source_count = ""# Intially 0 by default, but if old source, then database-defined, ask databse how many times this source has been added to, 
    source_method = input("Enter source method: ") #user-defined, list 1) Copied from OCR, 2) Copied from Internet, 3) Typed
    original_query = input("Enter original query: ")
    query_count = input("Enter query count: ")

    # Split the imported text into individual sentences using [ 。！？] as delimiters
    # Exclude delimiters that are within quotation marks
    sentences = re.split(r'(?<=[。！？])\s*(?![”])', text)
    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence.strip()]

    # Display the list of sentences before analysis
    print(f"{len(sentences)} sentences discovered:\n")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence.strip()}\n")

    # List of punctuation characters
    punctuation_chars = '"，。！？ , “ ” : ;'

    for i, sentence in enumerate(sentences, start=1):
        characters = list(sentence.strip())

        # Print the imported Chinese sentence
        print("-------------------------")
        print(f"Target Sentence {i}")
        print(f"Sentence: [{sentence.strip()}]")

        # Usage
        translated_text = translate_text(sentence, target_language="en")
        decoded_text = html.unescape(translated_text)
        print(f"Translated: [{decoded_text}]")
        print("-------------------------")

        # Ask for Vocabulary Analysis or Character Analysis or both
        analysis_choice = input("Choose analysis type:\n"
                                "1. Vocabulary Analysis\n"
                                "2. Character Analysis\n"
                                "3. Both\n"
                                "Enter your choice: ")
        print("-------------------------")

        vocab_analysis = analysis_choice in ('1', '3')
        char_analysis = analysis_choice in ('2', '3')

        # Vocab Analysis
        if vocab_analysis:
            jieba.initialize()  # (optional)
            seg_list = jieba.lcut(sentence, cut_all=False)
            print("Jieba Vocabulary Analysis:")
            # Filter out punctuation from the seg_list
            filtered_seg_list = [
                word for word in seg_list if word not in punctuation_chars
            ]

            # Account for duplicates, only show first occurrence
            unique_vocab_list = []
            for word in filtered_seg_list:
                if word not in unique_vocab_list:
                    unique_vocab_list.append(word)

            print(unique_vocab_list)  # Display unique vocabulary list
            # Analyze for learned vocab then against the full vocab
            learned_vocab = []
            learned_vocab_count = 0
            not_learned_vocab = []
            not_learned_vocab_count = 0
            unknown_vocab = []
            unknown_vocab_count = 0

            for term in unique_vocab_list:
                query_learned_vocab = f"SELECT * FROM learned_vocabulary WHERE term = '{term}'"
                cursor3.execute(query_learned_vocab)
                result_learned_vocab = cursor3.fetchone()

                if result_learned_vocab:
                    learned_vocab.append(term)
                    learned_vocab_count += 1
                else:
                    query_full_vocab = f"SELECT * FROM vocabulary WHERE term = '{term}'"
                    cursor4.execute(query_full_vocab)
                    result_full_vocab = cursor4.fetchone()

                    if result_full_vocab:
                        not_learned_vocab.append(term)
                        not_learned_vocab_count += 1
                    else:
                        unknown_vocab.append(term)
                        unknown_vocab_count += 1
            print("-------------------------")
            print(f"Learned Vocabulary: {learned_vocab_count} item(s)")
            print(learned_vocab)
            print("-------------------------")
            print(f"Not Learned Vocabulary: {not_learned_vocab_count} item(s)")
            print(not_learned_vocab)
            print("-------------------------")
            print(f"Unknown Vocabulary: {unknown_vocab_count} item(s)")
            print(unknown_vocab)
            print("-------------------------")

        # Character Analysis
        if char_analysis:
            total_hsk_sum = 0
            non_punctuation_count = 0

            for char in characters:
                if char in punctuation_chars:
                    status = "Punctuation"
                else:
                    query_learned = f"SELECT * FROM characters WHERE original = '{char}'"
                    cursor1.execute(query_learned)
                    result_learned = cursor1.fetchone()

                    if result_learned:
                        status = "Learned"
                    else:
                        query_info = f"SELECT * FROM full_characters WHERE character = '{char}'"
                        cursor2.execute(query_info)
                        result_info = cursor2.fetchone()

                        if result_info:
                            status = "Not Learned"
                            definition = result_info[5]
                            pinyin = result_info[3]
                            hsk_level = result_info[4]
                            total_hsk_sum += hsk_level
                            non_punctuation_count += 1
                        else:
                            status = "Unknown"
                            definition = "Unknown"  # Assign a default value to definition
                            pinyin = "Unknown"  # Assign a default value to pinyin
                            hsk_level = "Unknown"

                        print(f"Character: {char}\n"
                              f"Pinyin: {pinyin}\n"
                              f"Definition: {definition}\n"
                              f"HSK Level: {hsk_level}\n"
                              f"Status: {status}\n"
                              f"-------------------------")

            # Calculate average HSK level
            if non_punctuation_count != 0:
                average_hsk_level = total_hsk_sum / non_punctuation_count
                rounded_average_hsk = round(average_hsk_level, 2)
                print(
                    f"Average HSK Level of Characters in Sentence: {rounded_average_hsk}"
                )

    # Insert a record into the old historical usage database
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insert_query = f"INSERT INTO sentences (sentence, timestamp) VALUES ('{text}', '{timestamp}')"
    cursor_history.execute(insert_query)
    conn_history.commit()

    # Insert a record into the new usage_history database    
    # Example sentence data for a single query
    sentence_data = {
        "sentences": [
            {
                "text": "汪淼觉得...",
                "translation": "Wang Miao felt...",
                "vocab_analysis": {
                    "learned_vocab_list": ["汪淼", "觉得"],
                    "learned_vocab_count": 2,
                    "not_learned_vocab_list": ["奇怪", "组合"],
                    "not_learned_vocab_count": 2,
                    "unknown_vocab_list": [],
                    "unknown_vocab_count": 0,
                    "total_vocab_list": ["汪淼", "觉得", "奇怪", "组合"],
                    "total_vocab_count": 4
                },
                "char_analysis": {
                    "learned_char_list": ["汪", "淼"],
                    "learned_char_count": 2,
                    "not_learned_char_list": ["觉", "得"],
                    "not_learned_char_count": 2,
                    "unknown_char_list": [],
                    "unknown_char_count": 0,
                    "total_char_list": ["汪", "淼", "觉", "得"],
                    "avg_hsk_char_level": 3
                }
            },
            # Add more sentences and their analysis details here
        ]
    }

    # Convert the sentence data to JSON format
    sentence_data_json = json.dumps(sentence_data, ensure_ascii=False)

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
    
    cursor_usage_history.execute(insert_query, (
        source_type,
        source_id,
        source_title,
        source_count,
        source_method,
        original_query,
        query_count,
        sentence_data_json
    ))
    
    conn_usage_history.commit()


    # Close the database connection
    conn1.close()
    conn2.close()
    conn_history.close()

    # Offer options
    print("What would you like to do next?")
    print("1. Return to the main menu")
    print("2. Analyze another sentence")
    user_choice = input("Enter your choice: ")

    print("-------------------------")
    if user_choice == "1":
        return  # Return to the main menu
    elif user_choice == "2":
        user_sentence = input("Enter the new sentence for analysis: ")
        capture_and_analyze(user_sentence)  # Analyze another sentence
    else:
        print("Invalid choice. Returning to the main menu.")
