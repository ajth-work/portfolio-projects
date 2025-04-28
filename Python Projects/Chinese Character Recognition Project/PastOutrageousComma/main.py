# pip install jieba
# pip install google-auth==1.35.0
# pip install google-cloud-translate==2.0.1

import sqlite3
import jieba
import os

from my_programs.analyze.analyze_original import analyze_original
from my_programs.view_character_history.view_character_history import view_character_history_simple, view_character_history_detailed
from my_programs.view_historical_usage.view_historical_usage import view_historical_usage
from my_programs.view_sentence_history.view_sentence_history import view_sentence_history

from my_programs.analyze.database_connections import (
    conn1, conn2, conn3, conn4, conn_history, conn_usage_history, cursor1,
    cursor2, cursor3, cursor4, cursor_history, cursor_usage_history)
from my_programs.analyze.test_samples import test_sample_long, test_sample_short
from my_programs.imports.imports import linebreak
from my_programs.analyze.analyze_data_insertion import analyze_data_insertion

from bs4 import BeautifulSoup
import requests
from my_programs.duolingo.duome import fetch_and_print_words_learned


# Function to display the main menu
def main_menu():
    while True:

        menu_choices = [
            "Quick Analysis", "Analyze Your Own Sentence",
            "Analyze Short Test Sample", "Analyze Long Test Sample",
            "View Historical Usage", "View Character History",
            "View Sentence History", "Duolingo", "Exit"
        ]

        print("Welcome to Your Chinese Learning App!")
        print(f"{linebreak}\n")
        for i, choice in enumerate(menu_choices, start=1):
            print(f"{i}. {choice}\n")
        print(linebreak)
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            user_sentence = input(
                "Enter the sentence you want to quickly analyze: ")
            analyze_original(user_sentence)
        elif user_choice == '2':
            user_sentence = input("Enter the sentence you want to analyze: ")
            analyze_original(user_sentence)
        elif user_choice == '3':
            analyze_original(test_sample_short)
        elif user_choice == '4':
            analyze_original(test_sample_long)
        elif user_choice == '5':
            view_historical_usage()
        elif user_choice == '6':
            print(linebreak)
            print("View Character History Options:\n")
            print("1. Simple View (10 characters per line)\n")
            print("2. Detailed View\n")

            view_choice = input("Enter your view choice: ")
            print(linebreak)

            if view_choice == '1':
                view_character_history_simple()
            elif view_choice == '2':
                view_character_history_detailed()
            else:
                print("Invalid choice. Please enter '1' or '2'.")
        elif user_choice == '7':
            print(linebreak)
            view_sentence_history()
        elif user_choice == '8':
            fetch_and_print_words_learned(os.environ['DUOLINGO_USERNAME'])
        elif user_choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


# Call the main menu function
main_menu()
