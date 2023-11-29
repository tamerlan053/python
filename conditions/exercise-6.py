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
