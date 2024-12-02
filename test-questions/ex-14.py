Problem

# Write a Python function to determine if a given string contains balanced parentheses. 
# A string is considered balanced if every opening parenthesis ( has a corresponding closing parenthesis ) in the correct order.

def is_balanced(s):
    stack = []
    
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

# Example usage:
print(is_balanced("(()())"))  # Output: True
print(is_balanced("(()"))     # Output: False
