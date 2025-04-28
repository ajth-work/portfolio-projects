import sqlite3

conn = sqlite3.connect('learned_character_database.db')

cursor = conn.cursor()

# Provided Chinese sentence
sentence = "我喜欢学习中文。"

# Extract individual characters from the sentence
characters = list(sentence)

# Check each character in the database
for char in characters:
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
