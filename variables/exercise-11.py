# A phone company charges its customers a fixed amount of 20 euros every two months (connection, rental, maintenance).
# A phone call within Belgium costs 12 euro cents (regardless of the duration of the call), and an international call costs 50 euro cents per started minute.
# These rates do not include VAT.

# You enter the number of Belgian calls and the number of minutes spent on international calls in the past month via the keyboard.
# The program calculates the total payment for the past month. The VAT rate is 21%.


VAT_PERCENTAGE = 0.21

belgian_calls = int(input("Enter the number of Belgian calls: "))
foreign_calls = int(input("Enter the number of foreign calls: "))

fixed_amount = 20

price_belgian = belgian_calls * 0.12
price_foreign = foreign_calls * 0.5

price = price_belgian + price_foreign + fixed_amount / 2
with_vat = price * (1 + VAT_PERCENTAGE)

print("To pay: ", with_vat, "euros")
