# Exercise 8

# Cyclists are participating in an individual time trial covering a distance of 36 km.
# The registration number and time in seconds of each cyclist are entered via the keyboard.
# The input process stops when a negative number is entered for the registration number.
# It is assumed that each cyclist has a different time.

# Questions:
# Who is the fastest cyclist?
# What percentage of cyclists take longer than 1 hour?

sum = 0
counter = 0
formula = 60 * 60
total_cyclists = 0
fastest = 0
fastest_cyclist = 0

cyclist = int(input("Enter the cyclist's number: "))

while cyclist > 0:
    total_cyclists += 1

    time = int(input('Enter the time in seconds for this cyclist: '))

    if time > formula:
        counter += 1

    if time < 10000000:
        fastest = time
        fastest_cyclist = cyclist

    cyclist = int(input("Enter the cyclist's number: "))

hours = time // 3600
remaining_seconds = time % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("The percentage of cyclists is:", (counter / total_cyclists) * 100)
print("The fastest cyclist is the one with number:", fastest_cyclist)
print(hours, "h", minutes, "min", seconds, "sec")
