import sqlite3

conn = sqlite3.connect('learned_character_database.db')

cursor = conn.cursor()

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
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            status = "Learned"
        else:
            status = "Not Learned"

    print(f"Character: {char} | Status: {status}")

# Close the database connection
conn.close()
