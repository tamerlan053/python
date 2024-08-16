# Exercise 7

# The results of a student obtained in 3 different exams must be entered via the keyboard. These results are out of 20, and only whole numbers are given. Determine the percentage obtained by this student and print it along with the corresponding grade:

# < 60% insufficient
# < 70% sufficient
# < 80% distinction
# < 90% high distinction
# ≥ 90% highest distinction.

result_1 = int(input("Enter result 1: "))
result_2 = int(input("Enter result 2: "))
result_3 = int(input("Enter result 3: "))

total = ((result_1 + result_2 + result_3) / 60) * 100
grade = ""

if total < 60:
    grade = "insufficient"
elif total < 70:
    grade = "sufficient"
elif total < 80:
    grade = "distinction"
elif total < 90:
    grade = "high distinction"
else:
    grade = "highest distinction"

print("The student's percentage is", total, "and their grade is", grade)
