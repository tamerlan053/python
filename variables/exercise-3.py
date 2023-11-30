# Enter your height (in meters) and weight (in kilograms) via the keyboard.
# Calculate your BMI and print it.

height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

bmi = weight / (height * height)

print(bmi)

