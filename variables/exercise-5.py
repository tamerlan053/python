# You enter the number of degrees Fahrenheit via the keyboard, and the computer calculates the number of degrees Celsius, rounded to one decimal place.
# This value is then printed.

temp_fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))

formula_celsius = (temp_fahrenheit - 32) * (5 / 9)

print(round(formula_celsius, 1))
