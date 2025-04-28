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
        query = f"SELECT * FROM characters WHERE original = '{char}'"
        cursor1.execute(query)
        result = cursor1.fetchone()
        if result:
            status = "Learned"
        else:
            status = "Not Learned"

    print(f"Character: {char} | Status: {status}")

# Close the database connection
conn1.close()
conn2.close()

# Current status is that there are multiple connections with initialization, but no querying setup for presenting information about "Not Learned" content. Next steps are to implement formatted and dynamic responses to each not learned character.

# Additional direction is when reviewing character by character in the initial analysis, if status is "Learned" or "Not Learned", pull the HSK level for the character and add it to a ongoing sum, then divide by the count of non-punctuation characters to understand the average HSK level of all chinese characters in the sentence.
