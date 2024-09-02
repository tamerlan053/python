Problem

# Write a program to calculate the final price for hotel bookings. 
# For each booking, the following information is entered via the keyboard: customer name, number of nights, room type (single, double, suite), and whether the customer is a member of the hotel's loyalty program.
# Input ends when X or x is entered for the customer name.

# For each customer, the name and final price should be printed.
# The price is calculated as follows:
# -Base price per night: 
#   Single: €50, Double: €90, Suite: €150;
# -A discount of 10% for loyalty program members;
# -If the booking is for more than 5 nights, a discount of 5%;
# -A maximum total discount of 20% is allowed;
# -The final price must not be lower than €100, regardless of the discounts.

# The calculation of the final price takes place in a function.

def calculate_final_price(nights, room_type, is_member):
    BASE_PRICES = {
        'single': 50,
        'double': 90,
        'suite': 150
    }
    total_price = nights * BASE_PRICES[room_type]
    
    discount = 0

    if is_member:
        discount += 10  # 10% discount for loyalty members
    
    if nights > 5:
        discount += 5  # 5% discount for bookings over 5 nights
    
    if discount > 20:
        discount = 20  # Max discount is 20%

    final_price = total_price * (1 - discount / 100)
    
    if final_price < 100:
        final_price = 100  # Minimum price is €100
    
    return final_price
