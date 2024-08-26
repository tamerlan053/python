# Exercise 11

# The following data about employees of a company are entered:
# -Employee number
# -Gender: 0 = female; 1 = male
# -Age
# -Gross salary

# The input ends when the employee number 0 is entered. Ensure input validation for gender.

# Print the number of male employees who are older than 34 years, or have a salary of 1800 euros or more.
# Print the number of female employees who are younger than 25 years.

number = int(input("Enter your employee number: "))
male_count = 0
female_count = 0

while number != 0:
    gender = int(input("Enter your gender (0=female, 1=male): "))

    while gender != 0 and gender != 1:
        gender = int(input("Incorrect gender: enter again (0=female, 1=male): "))

    age = int(input("Enter your age: "))
    gross_salary = int(input("Enter your gross salary: "))

    if (gender == 1):
        if (age > 34 or gross_salary >= 1800):
            male_count += 1
    else:
        if (age < 25):
            female_count += 1

    number = int(input("Enter your employee number: "))

print("The number of men who meet the condition is", male_count)
print("The number of women who meet the condition is", female_count)
