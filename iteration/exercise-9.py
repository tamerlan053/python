# Exercise 9

# Write a program that prints the multiplication tables for the numbers 2 to 5 (inclusive).

for i in range(2, 6):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
