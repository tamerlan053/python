VAT_PERCENTAGE = 0.21

belgian_calls = int(input("Enter the number of Belgian calls: "))
foreign_calls = int(input("Enter the number of foreign calls: "))

fixed_amount = 20

price_belgian = belgian_calls * 0.12
price_foreign = foreign_calls * 0.5

price = price_belgian + price_foreign + fixed_amount / 2
with_vat = price * (1 + VAT_PERCENTAGE)

print("To pay: ", with_vat, "euros")
