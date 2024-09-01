# Exercise 3

# Write a program to calculate the membership fee for a tennis club. For each member, the following information is entered via the keyboard: name, age, number of children, income, and year of joining. Input ends when X or x is entered for the name.

# For each member, the name and membership fee should be printed.
# The membership fee is calculated as follows:
# -normal starting fee €100 per year;
# -members older than 60 years: a reduction of €15;
# -members with children a reduction of €7.5 per child with a maximum of €35;
# -members who have been a member for more than 20 years a reduction of €12.5;
# -members with an income less than €7500 per year a reduction of €25.

# The reductions can be accumulated but the minimum membership fee is €50.
# The calculation of the membership fee takes place in a function.

def calculate_membership_fee(age,children, joining_year, income):
    INITIAL_FEE = 100
    CURRENT_YEAR = 2023
    total = INITIAL_FEE

    if age > 60:
        total -= 15

    if children > 4:
        total -= 35
    else:
        total -= (children * 7.5)

    if (CURRENT_YEAR - joining_year) > 20:
        total -= 12.5

    if income < 7500:
        total -= 25

    if total < 50:
        total = 50

    return total
