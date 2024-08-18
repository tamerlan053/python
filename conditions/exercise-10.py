# Exercise 10

# Write a program that allows the input of the age and the year of joining of a member of a tennis club, and based on this information calculates and prints their contribution. The following rules are to be followed:

# -Base amount: 100 euros
# -Discount: 14.5 euros if the member is younger than 21 or older than 60
# -Discount: 2.5 euros per year of membership

# The minimum amount to be paid is 62.5 euros.

# Use a constant with the value of the current year.

BASIS = 100
CURRENT_YEAR = 2023

age = int(input("Enter your age: "))
year_of_joining = int(input("Enter your year of joining the club: "))

price = BASIS

if age < 21 or age > 60:
    price -= 14.5

price -= 2.5 * (CURRENT_YEAR - year_of_joining)

if price < 62.5:
    price = 62.5

print("The contribution for this member is:", price)
