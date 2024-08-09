Problem

# Write a function that determines if a given integer is a power of three.

def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# Examples
print(is_power_of_three(27))  # Output: True
print(is_power_of_three(9))   # Output: True
print(is_power_of_three(10))  # Output: False
