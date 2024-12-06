Problem

# Write a Python function to calculate the “majority element” in a list of integers. The majority element is the element that appears more than n // 2 times, where n is the size of the list. Assume the input list always has a majority element.

def majority_element(nums):
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate

# Example usage:
nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(result)  # Output: 2
