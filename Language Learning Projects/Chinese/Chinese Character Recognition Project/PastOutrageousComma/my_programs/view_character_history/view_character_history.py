import sqlite3
from my_programs.imports.imports import linebreak


# Function to view character history in a simple format (10 characters per line)
def view_character_history_simple():
    # Connect to the character analysis database
    conn_character = sqlite3.connect('my_databases/character_history.db')
    cursor_character = conn_character.cursor()

    # Query all character analysis records
    cursor_character.execute("SELECT character FROM character_history")
    characters = cursor_character.fetchall()

    # Check if there are any character analysis records
    if len(characters) == 0:
        print("No character analysis records found.")
    else:
        print("Character History (Simple View):")
        for i, character in enumerate(characters, start=1):
            print(character[0], end=", ")

            # Print a newline after every 10 characters
            if i % 10 == 0:
                print()
        print(f"\n{linebreak}")
    # Close the database connection
    conn_character.close()


# Detailed View (Original Code)
def view_character_history_detailed():

    # Connect to the character analysis database
    conn_character = sqlite3.connect('my_databases/character_history.db')
    cursor_character = conn_character.cursor()
    # Query all character analysis records
    cursor_character.execute(
        "SELECT character, analysis_count, character_info, timestamp FROM character_history"
    )
    character_records = cursor_character.fetchall()

    # Check if there are any character analysis records
    if len(character_records) == 0:
        print("No character analysis records found.")
    else:
        print("Character History (Detailed View):")
        for record in character_records:
            character, analysis_count, character_info, timestamp = record
            print(f"Character: {character}")
            print(f"Analysis Count: {analysis_count}")
            print(f"Character Info: {character_info}")
            print(f"Last Analysis Timestamp: {timestamp}")
            print("-------------------------")

    # Close the database connection
    conn_character.close()
