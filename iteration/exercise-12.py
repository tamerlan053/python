# Exercise 12

# A company wants to pay its employees a bonus that is proportional to the number of years of service. 
# Calculate the individual bonus and the total bonus. 
# For each employee, the following must be entered via the keyboard: the last name (entering "/" or "*" means the end of the program), first name, and the number of years of service. 
# Ensure input control for the number of years of service, it must be a number between 0 and 40 years. 
# The bonus is calculated as follows: the number of years of service * 25 euros. 
# If the number of years of service is less than 5, the person receives 0 euros as a bonus. Print the last name, first name, number of years of service, and bonus for each person. 
# At the end of the program, print the total bonus to be paid and the highest bonus.

last_name = input("Enter your last name: ")

total = 0
highest = 0

while last_name != "/" and last_name != "*":
    first_name = input("Enter your first name: ")
    years_of_service = int(input("Enter the number of years of service: "))

    while years_of_service < 0 or years_of_service > 40:
        years_of_service = int(input("Enter a correct number of years of service (between 0 and 40)"))

    if years_of_service < 5:
        bonus = 0
    else:
        bonus = years_of_service * 25

    if bonus > highest:
        highest = bonus

    total += bonus

    print("last_name =", last_name)
    print("first_name =", first_name)
    print("years_of_service =", years_of_service)
    print("bonus =", bonus)

    last_name = input("Enter your last name: ")

print("The total bonus to be paid is", total)
print("The highest bonus is", highest)
