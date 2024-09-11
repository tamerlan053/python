# Exercise 12

# Write a Python function longest_palindromic_substring(s) that takes a string s as input and returns the longest palindromic substring within s.
# A palindrome is a word, phrase, or sequence that reads the same backward as forward.

def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]

    start = 0
    max_len = 1

    for i in range(n):
        dp[i][i] = True
