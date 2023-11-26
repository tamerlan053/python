hours_1 = int(input("Enter the number of hours: "))
minutes_1 = int(input("Enter the number of minutes: "))
seconds_1 = int(input("Enter the number of seconds: "))

hours_2 = int(input("Enter the number of hours: "))
minutes_2 = int(input("Enter the number of minutes: "))
seconds_2 = int(input("Enter the number of seconds: "))

total_1 = (hours_1 * 3600) + (minutes_1 * 60) + seconds_1
total_2 = (hours_2 * 3600) + (minutes_2 * 60) + seconds_2

if total_1 > total_2:
    time_difference_seconds = total_1 - total_2
else:
    time_difference_seconds = total_2 - total_1

hours = time_difference_seconds // 3600
remaining_seconds = time_difference_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"The difference between the two times is: {hours} hours {minutes} minutes {seconds} seconds")
