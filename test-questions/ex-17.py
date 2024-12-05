Problem

# Write a Python function to find the longest word in a list of strings that can be built one character at a time by other words in the list.

# For example, if the input list is ["a", "banana", "app", "appl", "ap", "apply", "apple"], the function should return "apple".

# Explanation:
# "a" is a word.
# "ap" is built from "a".
# "app" is built from "ap".
# "appl" is built from "app".
# "apple" is built from "appl".

def longest_word(words):
    word_set = set(words)
    words.sort(key=lambda x: (-len(x), x))
    
    def can_build(word):
        for i in range(1, len(word)):
            if word[:i] not in word_set:
                return False
        return True
