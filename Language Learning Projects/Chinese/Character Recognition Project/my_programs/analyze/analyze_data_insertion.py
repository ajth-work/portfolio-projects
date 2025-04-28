import datetime
import sqlite3
import jieba
import string
import json

from my_programs.analyze.analyze_char import analyze_char
from my_programs.analyze.analyze_vocab import analyze_vocab
from my_programs.analyze.analyze_translate import analyze_translate

jieba.setLogLevel(20)


def analyze_data_insertion(sentence):
    # Initialize JSON data storage list
    sentence_data = {
        "Sentence": sentence.strip(),
        #"Sentence Note": None,
        "Translation": analyze_translate(sentence),
        #"Translation Note": None,
        "Vocabulary Analysis": analyze_vocab(sentence),
        #"Character Analysis": analyze_char(sentence)
    }
    for k, v in sentence_data.items():
        print(f"{k} - {v}\n")
