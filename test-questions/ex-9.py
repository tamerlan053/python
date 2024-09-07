# Exercise 9

# Write a Python program that reads a paragraph of text from the user and counts the frequency of each word in the text. 
# The program should then display the words in order of frequency, from most common to least common. 
# If two words have the same frequency, display them in alphabetical order.

### Requirements:
# -Ignore case when counting words (i.e., "The" and "the" should be treated as the same word).
# -Ignore punctuation (e.g., "hello!" and "hello" should be treated as the same word).
# -Words with the same frequency should be sorted alphabetically.

import string
from collections import Counter

def word_frequency_counter(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_count = Counter(words)
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_words:
        print(f"{word}: {count}")

text = input("Enter a paragraph of text: ")
word_frequency_counter(text)
