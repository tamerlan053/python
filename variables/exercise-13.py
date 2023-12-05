# How many revolutions will a wheel have to make to cover a given distance of m?
# The diameter of the bicycle wheel is provided in inches (see previous question).
# The following data is input: diameter of the bicycle wheel and the distance to be covered.


import math

diameter = int(input("Enter the diameter of a wheel: "))
distance = float(input("Enter the distance you want to cover: "))

distance_covered_in_meters = diameter * math.pi * 0.0254
calculation = distance / distance_covered_in_meters

print("The number of revolutions your wheel needs to make to cover", distance, "meters is:", calculation)
