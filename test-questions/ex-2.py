Problem

# Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

# Examples
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
