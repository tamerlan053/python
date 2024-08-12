# Exercise 2

# Enter the gross salary of an employee via the keyboard. The task is to calculate and print the annual holiday allowance and the annual contribution. The holiday allowance is 5% of the gross salary. If this holiday allowance is at least 350 euros, the annual contribution is equal to 8% of 350 euros. If the holiday allowance is less than 350 euros, the annual contribution is 8% of the holiday allowance.
# Print the following for this employee:

# -gross salary
# -holiday allowance
# -annual contribution

gross_salary = float(input("Enter the gross salary: "))

holiday_allowance = 0.05 * gross_salary

if holiday_allowance >= 350:
    annual_contribution = 0.08 * 350
else:
    annual_contribution = 0.08 * holiday_allowance

print("The gross salary of this employee is:", gross_salary)
print("The holiday allowance of this employee is:", holiday_allowance)
print("The annual contribution of this employee is:", annual_contribution)
