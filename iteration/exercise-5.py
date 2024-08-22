# Exercise 5

# Write a program that requests a number between 1 and 100 (exclusive). Ensure that any incorrect input is rejected.
# Whenever an incorrect input occurs, display an error message on the screen. 
# Either "Error! The number must be greater than 1" or "Error! The number must be less than 100".
# The program stops when a correct input is provided. The number is then displayed on the screen.

number = int(input("Enter a number between 1 and 100 (exclusive): "))

while number <= 1 or number >= 100:
    if number <= 1:
        print("Incorrect input! The number must be greater than 1!")
    elif number >= 100:
        print("Incorrect input! The number must be less than 100!")
    number = int(input("Enter a number between 1 and 100 (exclusive): "))

print("The correctly entered number is:", number)
