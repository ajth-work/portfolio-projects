from my_programs.imports.imports import linebreak


def calculate_average_hsk(total_hsk_sum, non_punctuation_count):
    if non_punctuation_count != 0:
        rounded_average_hsk = round((total_hsk_sum / non_punctuation_count), 2)
        print(
            f"Average HSK Level of Not Learned Characters in Sentence: {rounded_average_hsk}"
        )
        return rounded_average_hsk
