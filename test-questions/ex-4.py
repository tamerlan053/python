Problem

# Write a function to determine if a string has all unique characters.

def has_unique_characters(s):
    return len(s) == len(set(s))
