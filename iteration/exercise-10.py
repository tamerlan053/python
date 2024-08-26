# Exercise 10

# Write a program that uses nested loops to produce the following screen output.
# The size of the triangle is provided via input from the keyboard.
# For your information: the height and width of the triangle are equal.

height = int(input("Enter the height of the triangle "))

for i in range(height, 0, -1):
    for j in range(i):
        print("@", end=" ")
    print()
