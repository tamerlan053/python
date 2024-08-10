Problem

# Write a function to determine if a string has all unique characters.

def has_unique_characters(s):
    return len(s) == len(set(s))

# Examples
print(has_unique_characters("abcdef"))  # Output: True
print(has_unique_characters("hello"))   # Output: False
