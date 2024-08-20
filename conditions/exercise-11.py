# Exercise 11

# Price Calculation for a Holiday

# Input:
# - Number of stars: 1 - 5
# - Code: O (only breakfast), H (half-board), V (full-board), A (all-inclusive)
# - Number of nights
# - Season: H (high season), L (low season), T (mid season)

# The price for accommodation is calculated as follows:
# - For a 1-star hotel, you pay 30 euros per night
# - For a 2-3 star hotel, you pay 40 euros per night
# - For a 4-5 star hotel, you pay 55 euros per night

# The price for meals is calculated as follows:
# - For only breakfast, you pay 20% of the accommodation costs
# - For half-board, you pay 50% of the accommodation costs
# - For full-board, you pay 60% of the accommodation costs

# NOTE: For All-inclusive, you always pay (regardless of the number of stars) 
# an additional fixed price of 80 euros per night on top of the full-board price.

# An extra discount of 10% on the total price is given during the low season for codes O and H.
# Enter the necessary information and print the price of a holiday for one person.

stars = int(input("Enter the number of stars (1 - 5): "))
code = input("Enter the code: ")
overnights = int(input("Enter the number of overnights: "))
season = input("Enter the season: ")

night_price = 0

if stars == 1:
    night_price = 30
elif stars == 2 or stars == 3:
    night_price = 40
else:
    night_price = 55

if code == "O":
    night_price = night_price + (night_price * 0.2)
elif code == "H":
    night_price = night_price + (night_price * 0.5)
elif code == "V":
    night_price = night_price + (night_price * 0.6)
elif code == "A":
    night_price = night_price + (night_price * 0.6 + 80)
