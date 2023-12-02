# Can you think of a way to swap the contents of two numeric variables without using a third auxiliary variable?


a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

a = a + b
b = a - b
a = a - b

print(a, b)
