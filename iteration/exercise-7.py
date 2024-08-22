# Exercise 7

# Read the temperature measured at 12:00 noon for 10 days via the keyboard.
# Requested output: + the highest temperature for these 10 days + the average temperature for these 10 days.

count = 0
total = 0
highest_temperature = -100

for i in range(10):
    count += 1
    temperature = float(input("Enter the temperature for day " + str(count) + ": "))
    total += temperature
    if temperature > highest_temperature:
        highest_temperature = temperature

print("The average temperature is:", total / count)
print("The highest temperature is:", highest_temperature)
