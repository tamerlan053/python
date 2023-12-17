number = int(input("Enter a number between 1 and 100 (exclusive): "))

while number <= 1 or number >= 100:
    if number <= 1:
        print("Incorrect input! The number must be greater than 1!")
    elif number >= 100:
        print("Incorrect input! The number must be less than 100!")
    number = int(input("Enter a number between 1 and 100 (exclusive): "))

print("The correctly entered number is:", number)
