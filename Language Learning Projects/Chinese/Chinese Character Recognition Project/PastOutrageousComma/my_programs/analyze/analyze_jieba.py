import jieba
from my_programs.analyze.analyze_get_char_details import get_char_details
from my_programs.analyze.analyze_punctuation import punctuation_chars, alphabet_chars, number_chars


def analyze_jieba(sentence):
    jieba.setLogLevel(20)
    jieba.initialize()  # (optional)

    reading_output = ""

    seg_list = jieba.lcut(sentence, cut_all=False)
    print("SEGLIST", seg_list)
    for item in seg_list:
        if item != "\n":
            reading_output += item

    print("READINGOUTPUT: ", reading_output)

    #contact full character database
    #check if character is punctuation, if not then go directly to full character database
    #if punctuation, then put that punctuation on the pinyin reading output text

    pinyin_reading = ""

    for char in reading_output:
        if char in punctuation_chars or alphabet_chars or number_chars:
            print("PAN", char)
            #pinyin_reading += char
        else:
            print("ZH", char)
            #pinyin_reading += char
            pinyin_reading += "1"

    print("PINYIN READING1", pinyin_reading)

    #print("Jieba Vocabulary Analysis:")
    # Filter out punctuation from the seg_list
    filtered_seg_list = [
        word for word in seg_list if word not in punctuation_chars
    ]

    # Account for duplicates, only show first occurrence
    unique_vocab_list = []
    for word in filtered_seg_list:
        if word not in unique_vocab_list:
            unique_vocab_list.append(word)

    #print(unique_vocab_list)  # Display unique vocabulary list
    return seg_list, filtered_seg_list, unique_vocab_list, reading_output
