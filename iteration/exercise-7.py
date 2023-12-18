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
