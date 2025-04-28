import sqlite3

# Define database connections
conn1 = sqlite3.connect('my_databases/learned_character_database.db')
conn2 = sqlite3.connect('my_databases/full_character_database.db')
conn3 = sqlite3.connect('my_databases/learned_vocabulary_database.db')
conn4 = sqlite3.connect('my_databases/full_vocabulary_database.db')
conn_history = sqlite3.connect('my_databases/historical_usage.db')
conn_usage_history = sqlite3.connect('my_databases/usage_history.db')

# Define cursor variables
cursor1 = conn1.cursor()
cursor2 = conn2.cursor()
cursor3 = conn3.cursor()
cursor4 = conn4.cursor()
cursor_history = conn_history.cursor()
cursor_usage_history = conn_usage_history.cursor()
