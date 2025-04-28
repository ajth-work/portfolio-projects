import datetime
import sqlite3
import string
import re
import html
import json

from my_programs.analyze.analyze_jieba import analyze_jieba

from my_programs.analyze.database_connections import (
    conn1, conn2, conn3, conn4, conn_history, conn_usage_history, cursor1,
    cursor2, cursor3, cursor4, cursor_history, cursor_usage_history)
from my_programs.imports.imports import linebreak


def analyze_vocab(text):
    seg_list, filtered_seg_list, unique_vocab_list, reading_output = analyze_jieba(text)

    # Analyze for learned vocab then against the full vocab
    # lv - learned vocab, nlv - not learned vocab, uv - unknown vocab, tv - total vocab

    learned_vocab, not_learned_vocab, not_learned_vocab_full_result, unknown_vocab, total_vocab = [], [], [], [], []
    learned_vocab_count, not_learned_vocab_count, unknown_vocab_count, total_vocab_count = 0, 0, 0, 0
    learned_vocab_hsk_level, not_learned_vocab_hsk_level, total_vocab_hsk_level = 0, 0, 0

    for term in unique_vocab_list:
        # Add term to the total vocab list
        total_vocab.append(term)
        total_vocab_count += 1

        # Check if term is in the learned vocab database
        query_learned_vocab = "SELECT * FROM learned_vocabulary WHERE term = ?"
        cursor3.execute(query_learned_vocab, (term, ))
        result_learned_vocab = cursor3.fetchone()

        # If term is in the learned vocab database
        if result_learned_vocab:
            #print("Learned Vocab Finds:\n", result_learned_vocab)
            learned_vocab.append(term)
            learned_vocab_count += 1
            learned_vocab_hsk_level += result_learned_vocab[4]
            total_vocab_hsk_level += result_learned_vocab[4]

        # Check if the term is in the full vocab database
        else:
            query_full_vocab = "SELECT * FROM vocabulary WHERE term = ?"
            cursor4.execute(query_full_vocab, (term, ))
            result_full_vocab = cursor4.fetchone()

            # If term is in the full vocab database
            if result_full_vocab:
                print("Full Vocab Finds:\n", result_full_vocab)
                not_learned_vocab.append(term)
                not_learned_vocab_full_result.append(result_full_vocab)
                not_learned_vocab_count += 1
                not_learned_vocab_hsk_level += result_full_vocab[4]
                total_vocab_hsk_level += result_full_vocab[4]

            # If term is not found in either learned or full vocab databases
            else:
                unknown_vocab.append(term)
                unknown_vocab_count += 1

    # Set up average HSK level math
    # Broke on following example: 你好。我住在中国。我很高兴认识你。
    # Calculate average HSK level for not learned vocabulary
    avg_not_learned_vocab_hsk_level = 0  # Initialize to zero
    if not_learned_vocab_count > 0:  # Check for non
        avg_not_learned_vocab_hsk_level = not_learned_vocab_hsk_level / not_learned_vocab_count

    # Calculate average HSK level for learned vocabulary
    avg_learned_vocab_hsk_level = 0
    if learned_vocab_count > 0:
        avg_learned_vocab_hsk_level = learned_vocab_hsk_level / learned_vocab_count

    # Calculate net_total_vocab_count
    net_total_vocab_count = total_vocab_count - unknown_vocab_count

    # Calculate average HSK level for all learned and not learned vocabulary
    avg_total_vocab_hsk_level = 0
    if net_total_vocab_count > 0:
        avg_total_vocab_hsk_level = total_vocab_hsk_level / net_total_vocab_count

    # Total Vocab Export
    print("TOTAL VOCAB", total_vocab)

    # Set up export items
    lv = "Learned", learned_vocab_count, learned_vocab, avg_learned_vocab_hsk_level
    nlv = "Not Learned", not_learned_vocab_count, not_learned_vocab, avg_not_learned_vocab_hsk_level
    uv = "Unknown", unknown_vocab_count, unknown_vocab
    tv = "Total", total_vocab_count, total_vocab, avg_total_vocab_hsk_level
    final_v = lv, nlv, uv, tv

    #for v in final_v:
    #print(linebreak)
    #print(f"{v[0]} Vocabulary: {v[1]} item(s)\n {v[2]}")
    #print(linebreak)
    #print(final_v)

    return final_v
