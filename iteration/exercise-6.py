# Enter the article number, quantity, and unit price via the keyboard. The input ends when the article number is 999. Requested output:
# Print the details for each article (article number, quantity, unit price, amount).
# Display the total amount to be paid for the purchase.


total_amount = 0

article = int(input("Enter article number: "))

while article != 999:
    unit_price = int(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))
    calculation = quantity * unit_price
    print("Article number =", article, "/", "Quantity =", quantity, "/", "Unit price =", unit_price, "/", "Amount:",
          calculation)
    total_amount += calculation
    article = int(input("Enter article number: "))

print("The total amount of the purchase is:", total_amount)
