# Exercise 4

# Write a program to calculate a person's weight on the Moon, Jupiter, and Mars. 
# The weight should vary between 50 kg and 120 kg in increments of 5 kg. 
# The following constants are used in your program: percentage of weight relative to Earth - Moon: 16.5%, Jupiter: 253.7%, and Mars: 37.8%

MOON = 0.165
JUPITER = 2.537
MARS = 0.378

for i in range(50, 121, 5):
    print("Earth: ", i)
    print("Moon: ", i * MOON)
    print("Jupiter: ", i * JUPITER)
    print("Mars: ", i * MARS)
    print()
