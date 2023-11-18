ADULT_PRICE = 11
CHILD_PRICE = 6

number_of_adults = int(input("Enter the number of adults: "))
number_of_children = int(input("Enter the number of children: "))

total_price = (ADULT_PRICE * number_of_adults) + (CHILD_PRICE * number_of_children)

print(total_price)
