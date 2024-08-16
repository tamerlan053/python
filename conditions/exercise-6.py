# Exercise 6

# Create a program to calculate the purchase price of a DVD. Input the year of the film and its rating (a number between 1-5) via the keyboard. The base price is always 5 euros. For a film that is less than 2 years old, an additional euro is added. For films with a rating of 4 or 5, you pay 2 euros more. Print the price of the film.

# Extension:
# + For films with a rating of 3 or 2, you pay 1 euro more.
# + Make sure that a film never costs more than 7 euros.

BASE_PRICE = 5

year = int(input("Enter the release year of the film: "))
rating = int(input("Enter the rating of the film (1-5): "))

price = BASE_PRICE

year_difference = 2023 - year

if year_difference < 2:
    price += 1

if rating == 5 or rating == 4:
    price += 2
elif rating == 3 or rating == 2:
    price += 1

if price > 7:
    price = 7

print("The price of a movie is:", price)
