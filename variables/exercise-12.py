# The diameter of a bicycle wheel is usually specified in inches (1 inch = 0.0254 m).
# Determine the revolution of a wheel expressed in meters, given a diameter in inches, and print the result obtained.

# Diameter of a wheel: 
# Distance traveled in one revolution: 
# Distance traveled in meters: 


import math

diameter = int(input("Enter the diameter of a wheel: "))
inch_in_m = 0.0254
distance_traveled = diameter * math.pi
distance_traveled_in_m = distance_traveled * inch_in_m

print("The distance traveled in inches for one revolution is:", distance_traveled)
print("The distance traveled in meters for one revolution is:", distance_traveled_in_m)
