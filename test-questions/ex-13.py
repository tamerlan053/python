Problem

# Given a list of strings, write a Python function to group anagrams together. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.

# For example, if the input list is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return:

from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
    
    return list(anagram_dict.values())
