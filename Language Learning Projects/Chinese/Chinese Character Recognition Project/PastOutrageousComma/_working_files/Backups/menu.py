# need to add import my program for the analyze and history functions
# also need to set analyze up to accept user submissions
import sqlite3

import jieba
from my_programs.capture_and_analyze.capture_and_analyze import capture_and_analyze
from my_programs.view_historical_usage.view_historical_usage import view_historical_usage


# Function to display the main menu
def main_menu():
    while True:
        choice = input("""Welcome to Your Chinese Learning App!\n
1. Analyze Your Own Sentence\n
2. Analyze Sample Text\n
3. View Historical Usage\n
4. Exit\n
Enter your choice: """)

        if choice == '1':
            user_sentence = input("Enter the sentence you want to analyze: ")
            capture_and_analyze(user_sentence)
        elif choice == '2':
            sample_text = "从一个“史无前例”的年代到另一个史无前例 的年代,从一种神秘的现 实到另一种神秘的现实, 刘慈欣新古典主义科幻小说的巅峰之作。"
            capture_and_analyze(sample_text)  # Using the sample text
        elif choice == '3':
            view_historical_usage()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


# Call the main menu function
main_menu()
