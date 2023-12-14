sum_total = 0
neg_count = 0
number = int(input("Enter an integer: "))

while number != 0:
    sum_total += number
    if number < 0:
        neg_count += 1
    number = int(input("Enter an integer: "))

print("The sum of the entered numbers is:", sum_total)
print("The number of negative entered numbers is:", neg_count)
