import sqlite3

conn1 = sqlite3.connect('learned_character_database.db')
conn2 = sqlite3.connect('full_character_database.db')

cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

# Provided Chinese sentence
sentence = "从一个“史无前例”的年代到另一个史无前例 的年代,从一种神秘的现 实到另一种神秘的现实, 刘慈欣新古典主义科幻小 说的巅峰之作。"

# Extract individual characters from the sentence
characters = list(sentence)

# List of punctuation characters
punctuation_chars = '"，。！？ , “ ”'  # Add any other punctuation marks you want to handle

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
                definition = result_info[
                    5]  # Assuming the meaning is in the second column
                pinyin = result_info[
                    3]  # Assuming the pronunciation is in the third column
                hsk_level = result_info[
                    4]  # Assuming levels are in the fourth column
            else:
                status = "Unknown"

            # Display the fetched information or build a response
            print(
                f"Character: {char}\n"
                f"Pinyin: {pinyin}\n"
                f"Definition: {definition}\n"
                f"HSK Level: {hsk_level}\n"
                f"Status: {status}\n"
                f"-------------------------", )

# Close the database connection
conn1.close()
conn2.close()

# Current status is that there are multiple connections with initialization, but no querying setup for presenting information about "Not Learned" content. Next steps are to implement formatted and dynamic responses to each not learned character.

# Additional direction is when reviewing character by character in the initial analysis, if status is "Learned" or "Not Learned", pull the HSK level for the character and add it to a ongoing sum, then divide by the count of non-punctuation characters to understand the average HSK level of all chinese characters in the sentence.

#Make a database of sentences tested, when, which words were okay, which were learned, etc.
