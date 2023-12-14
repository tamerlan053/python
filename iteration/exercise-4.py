MOON = 0.165
JUPITER = 2.537
MARS = 0.378

for i in range(50, 121, 5):
    print("Earth: ", i)
    print("Moon: ", i * MOON)
    print("Jupiter: ", i * JUPITER)
    print("Mars: ", i * MARS)
    print()
