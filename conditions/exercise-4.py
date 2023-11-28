number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 < number2:
    smallest_number = number1
    largest_number = number2
else:
    smallest_number = number2
    largest_number = number1

square_of_smallest = smallest_number * smallest_number

if smallest_number != 0:
    calculation = largest_number / smallest_number
else:
    calculation = "Attention, division by 0"

print("The smallest number is:", smallest_number)
print("The square of the smallest number is:", square_of_smallest)
print("The largest divided by the smallest is:", calculation)
