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
