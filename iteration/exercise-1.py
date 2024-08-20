# Exercise 1

# Prompt the user to input the weight of an apple in grams.
# Display a table of the weights of 1 to 100 apples.

weight = int(input("Enter the weight of an apple: "))

for i in range(1, 101):
    calculation = weight * i
    print(i, "apple(s) weight is", calculation, "g.")
