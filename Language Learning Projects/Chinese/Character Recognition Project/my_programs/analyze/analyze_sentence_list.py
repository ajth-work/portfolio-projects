import string
import re


def analyze_sentence_list(text):

    # Split the imported text into individual sentences using [ 。！？] as delimiters
    # Exclude delimiters that are within quotation marks
    sentences = re.split(r'(?<=[。！？])\s*(?![”])', text)
    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence.strip()]

    return sentences
