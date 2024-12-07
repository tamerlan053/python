Problem

# Write a Python function to find the first non-repeating character in a string. If all characters repeat, return None.

# For example:
# For the input "leetcode", the output should be "l".
# For the input "loveleetcode", the output should be "v".
# For the input "aabb", the output should be None.

from collections import Counter

def first_non_repeating_character(s):
    char_count = Counter(s)
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

# Example usage:
s = "loveleetcode"
result = first_non_repeating_character(s)
print(result)  # Output: "v"
