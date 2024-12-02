Problem

# Write a Python function to find all the unique elements in a list that appear exactly twice. 
# The function should return these elements in a new list.

# For example:
# If the input list is [1, 2, 3, 2, 4, 1, 5, 1], the function should return [2].
# If the input list is [4, 4, 3, 3, 2, 2], the function should return [4, 3, 2].

from collections import Counter

def find_elements_appearing_twice(nums):
    counts = Counter(nums)
    return [num for num, count in counts.items() if count == 2]

# Example usage:
nums = [1, 2, 3, 2, 4, 1, 5, 1]
result = find_elements_appearing_twice(nums)
print(result)  # Output: [2]
