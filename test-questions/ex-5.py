Problem

# Write a Python function that checks if a given string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward, such as "madam" or "racecar".

def is_palindrome(text):
  """
  Checks if a given string is a palindrome.

  Args:
      text: The string to check.

  Returns:
      True if the string is a palindrome, False otherwise.
  """
  text = text.lower()
  text = ''.join(c for c in text if c.isalnum())
  return text == text[::-1]

# Examples
print(is_palindrome("racecar"))   # Output: True
print(is_palindrome("madam"))    # Output: True
print(is_palindrome("apple"))    # Output: False
print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True
