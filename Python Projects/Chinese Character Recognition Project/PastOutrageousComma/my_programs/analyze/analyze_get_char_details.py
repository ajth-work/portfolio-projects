import sqlite3
import string

from my_programs.analyze.database_connections import (
    conn1, conn2, conn3, conn4, conn_history, conn_usage_history, cursor1,
    cursor2, cursor3, cursor4, cursor_history, cursor_usage_history)
from my_programs.analyze.analyze_punctuation import punctuation_chars
from my_programs.imports.imports import linebreak
from collections import OrderedDict


def get_char_details(char_position, char, total_hsk_sum,
                     non_punctuation_count):
    char_details = {
        "Position": char_position,
        "Character": char,
        "Pinyin": None,
        "Definition": None,
        "HSK Level": None,
        "Status": None
    }

    # if char is actually punctuation
    if char in punctuation_chars:
        char_details["Status"] = "Punctuation"

    #if char is not punctuation, check if learned
    else:
        query_learned = "SELECT * FROM characters WHERE original = ?"
        cursor1.execute(query_learned, (char, ))
        result_learned = cursor1.fetchone()

        # if char was learned previously
        if result_learned:
            char_details["Status"] = "Learned"
            char_details["Definition"] = result_learned[5]
            char_details["Pinyin"] = result_learned[3]
            char_details["HSK Level"] = result_learned[4]

        #if char is not learned, check if it's in full char database
        else:
            query_info = "SELECT * FROM full_characters WHERE character = ?"
            cursor2.execute(query_info, (char, ))
            result_info = cursor2.fetchone()

            # if char was not in learned but found in full char database
            if result_info:
                char_details["Status"] = "Not Learned"
                char_details["Definition"] = result_info[5]
                char_details["Pinyin"] = result_info[3]
                char_details["HSK Level"] = result_info[4]
                total_hsk_sum += char_details["HSK Level"]
                non_punctuation_count += 1

            # if char cannot be found in both databases
            else:
                char_details["Status"] = "Unknown"
                char_details["Definition"] = "Unknown"
                char_details["Pinyin"] = "Unknown"
                char_details["HSK Level"] = "Unknown"

    return char_position, char, char_details, total_hsk_sum, non_punctuation_count
