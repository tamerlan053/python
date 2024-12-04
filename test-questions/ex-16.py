Problem

# Write a Python function to determine if two strings are isomorphic. 
# Two strings are isomorphic if the characters in one string can be replaced to get the other string, with each character mapping uniquely.

# For example:
# The strings "egg" and "add" are isomorphic because e → a and g → d.
# The strings "foo" and "bar" are not isomorphic because o → a and o → r would conflict.
# The function should return True if the strings are isomorphic, and False otherwise.

def are_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    
    mapping_s1_to_s2 = {}
    mapping_s2_to_s1 = {}
    
    for char1, char2 in zip(s1, s2):
        if (char1 in mapping_s1_to_s2 and mapping_s1_to_s2[char1] != char2) or \
           (char2 in mapping_s2_to_s1 and mapping_s2_to_s1[char2] != char1):
            return False
        mapping_s1_to_s2[char1] = char2
        mapping_s2_to_s1[char2] = char1
    
    return True

# Example usage:
print(are_isomorphic("egg", "add"))  # Output: True
print(are_isomorphic("foo", "bar"))  # Output: False
