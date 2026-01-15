"""
Word Frequency Analyzer (First Principles)
Author: Anurag
Date: Jan 2026
Description: A custom implementation of a word counter without using 
the 'collections' library to demonstrate algorithmic logic.
"""


# Define the function

def analyse_frequency(raw_text):
    raw_text = raw_text.lower()
    raw_text = raw_text.replace("," , "").replace("." , "")
    text_list = raw_text.split(" ")
    word_count = {}
    for word in text_list:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

        highest_count = 0
        best_word = ""
        for word , count in word_count.items():
            if count > highest_count:
                highest_count = count
                best_word = word
                
    return best_word, highest_count
            


result_word, result_count = analyse_frequency("Python is great. Python is fast.")
print(f"Winner: {result_word} {result_count}")          