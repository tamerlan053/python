gross_salary = float(input("Enter the gross salary: "))

holiday_allowance = 0.05 * gross_salary

if holiday_allowance >= 350:
    annual_contribution = 0.08 * 350
else:
    annual_contribution = 0.08 * holiday_allowance

print("The gross salary of this employee is:", gross_salary)
print("The holiday allowance of this employee is:", holiday_allowance)
print("The annual contribution of this employee is:", annual_contribution)
