Problem

# Write a Python function called `calculate_average` that takes a list of numbers as input and returns the average of those numbers.

def calculate_average(numbers):
  if len(numbers) == 0:
    return 0
  total = sum(numbers)
  average = total / len(numbers)
  return average

# Examples
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"The average of the numbers is: {average}")
