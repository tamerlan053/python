# Exercise 3

# Calculate the arrival time of a flight. The departure time (hours and minutes in 2 different variables) and the duration in minutes are entered.  
# For example, if the departure hour is 22, the departure minute is 18, and the duration is 170 minutes, the arrival hour will be 1, and the arrival minute will be 8.

departure_hour = int(input("Enter departure hour: "))
departure_minutes = int(input("Enter departure minutes: "))
duration_in_minutes = int(input("Enter duration in minutes: "))

departure_time_in_minutes = departure_hour * 60
total_minutes = departure_time_in_minutes + departure_minutes + duration_in_minutes

arrival_time_in_hours = (total_minutes // 60) % 24
arrival_time_in_minutes = total_minutes % 60

print("You will arrive at:", round(arrival_time_in_hours), "hours and", arrival_time_in_minutes, "minutes!")
