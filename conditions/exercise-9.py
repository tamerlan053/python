# Exercise 9

# Via the keyboard, two integers \( a \) and \( b \) and an operation code are entered. The operation code offers the following options:
#  -Code 1: Addition (\( a + b \))
#  -Code 2: Subtraction (\( a - b \))
#  -Code 3: Multiplication (\( a \times b \))
#  -Code 4: Square of \( a \)
#  -Code 5: Square of \( b \)

# The goal is to perform the operation specified by the code on the entered numbers \( a \) and \( b \), and print the result along with the entered numbers. If a code is entered that does not correspond to one of the above operation codes, the message "Invalid code" should be printed.

a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))
code = int(input("Enter code (1=addition; 2=subtraction; 3=multiplication; 4=square of a; 5=square of b): "))

if code == 1:
    result = a + b
elif code == 2:
    result = a - b
elif code == 3:
    result = a * b
elif code == 4:
    result = a * a
elif code == 5:
    result = b * b
else:
    result = "Invalid code"

print("The 2 numbers are", a, "and", b, "and the result is", result)
