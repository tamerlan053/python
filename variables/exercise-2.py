# The entrance fee for a zoo is 11 euros for adults and 6 euros for children under 12 years old.
# Create a program that reads the number of adults and children from the keyboard and calculates and prints the total price.

ADULT_PRICE = 11
CHILD_PRICE = 6

number_of_adults = int(input("Enter the number of adults: "))
number_of_children = int(input("Enter the number of children: "))

total_price = (ADULT_PRICE * number_of_adults) + (CHILD_PRICE * number_of_children)

print(total_price)
