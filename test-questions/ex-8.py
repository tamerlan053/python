Problem

# Write a function that determines if a given integer is a factorial number.
# A factorial number is any number that can be written as n! = 1 * 2 * ... * n, where n is a non-negative integer.

def is_factorial(n):
    if n < 1:
        return False
    
    factorial = 1
    i = 1
    
    while factorial < n:
        i += 1
        factorial *= i
    
    return factorial == n
