# Exercise 8
# The price of a plane ticket is determined by several factors, namely:

# + The length of the flight or the distance in km
#    - <1000 km: short-distance flight: 25 euro cents/km
#    - 1000-2999 km: medium-distance flight: 20 euro cents/km
#    - >2999 km: long-distance flight: 12 euro cents/km
# + The type of flight or class:
#   - economy class
#   - charter -20%
#   - business trip +30%

# Write a program that calculates the price of a plane ticket. 
# The distance in km and the class (1 = economy class, 2 = charter, and 3 = business trip) must be entered. 
# Print the final ticket price. This price must be expressed in euros.

distance = int(input("Enter the flight distance (in km): "))
class_type = int(input("Enter the class of the flight (1=economy; 2=charter; 3=business): "))

price = 0

if distance < 1000:
    price = distance * 0.25
elif distance >= 1000 and distance <= 2999:
    price = distance * 0.2
else:
    price = distance * 0.12

if class_type == 2:
    price = price - (price * 0.2)
elif class_type == 3:
    price = price + (price * 0.3)

print("The price of your ticket is", price, "Euro")
