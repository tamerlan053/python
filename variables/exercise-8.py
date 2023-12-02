# What does my car cost? Price-conscious individuals want to know how much their car truly costs. Successively, the following is entered:

# number of kilometers traveled per year (traveled_km)
# consumption in liters per 100 km (consumption)
# price of 1 liter of fuel (price_per_liter)

# The expected output is:
# the total costs per year for the specified number of kilometers
# the cost per kilometer driven.


annual_distance_km = int(input("Enter the number of kilometers driven per year: "))
fuel_consumption_per_100km = float(input("Enter fuel consumption in liters per 100 kilometers: "))
price_of_1_liter = float(input("Enter the price of 1 liter of fuel: "))

total_cost_per_year = (annual_distance_km / 100) * fuel_consumption_per_100km * price_of_1_liter
cost_per_km = total_cost_per_year / annual_distance_km

print("The total annual cost for the specified number of kilometers is:", total_cost_per_year)
print("The cost per kilometer driven is:", cost_per_km)
