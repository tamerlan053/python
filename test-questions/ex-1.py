Problem

# Write a function that checks if two lists are permutations of each other. For example, the lists [1, 2, 3] and [3, 2, 1] are permutations of each other, while [1, 2, 3] and [1, 2, 2] are not.
def are_permutations(list1, list2):
    if len(list1) != len(list2):
        return False
    return sorted(list1) == sorted(list2)

list1 = [1, 2, 3]
list2 = [3, 2, 1]

print(are_permutations(list1, list2))  # Output: True

list3 = [1, 2, 3]
list4 = [1, 2, 2]

print(are_permutations(list3, list4))  # Output: False
