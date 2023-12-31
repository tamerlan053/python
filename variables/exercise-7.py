# Write a program that calculates the costs for installing wall-to-wall carpeting.
# The user of the program provides the length and width of the carpet (expressed in meters), the price per square meter, and the installation costs per square meter.
# The program should output the cost of the carpet, installation costs, and total costs.

length = float(input("Enter the length of the carpet: "))
width = float(input("Enter the width of the carpet: "))
price_per_square_meter = float(input("Enter the price per square meter: "))
placement_cost_per_square_meter = int(input("Enter the placement cost per square meter: "))

carpet_cost = (length * width) * price_per_square_meter
placement_cost = (length * width) * placement_cost_per_square_meter
total_cost = round(carpet_cost + placement_cost, 2)

print("The cost of the carpet:", carpet_cost)
print("The placement cost of the carpet is:", placement_cost)
print("The total cost is:", total_cost)
