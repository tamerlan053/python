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
