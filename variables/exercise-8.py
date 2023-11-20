annual_distance_km = int(input("Enter the number of kilometers driven per year: "))
fuel_consumption_per_100km = float(input("Enter fuel consumption in liters per 100 kilometers: "))
price_of_1_liter = float(input("Enter the price of 1 liter of fuel: "))

total_cost_per_year = (annual_distance_km / 100) * fuel_consumption_per_100km * price_of_1_liter
cost_per_km = total_cost_per_year / annual_distance_km

print("The total annual cost for the specified number of kilometers is:", total_cost_per_year)
print("The cost per kilometer driven is:", cost_per_km)
