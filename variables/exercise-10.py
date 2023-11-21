# swap the values of two variables without using an additional variable

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

a = a + b
b = a - b
a = a - b

print(a, b)
