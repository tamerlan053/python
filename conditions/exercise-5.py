VAT_PERCENTAGE = 0.21
ITEM_PRICE = 11.5

quantity = int(input("How many units do you want: "))

total_without_vat = quantity * ITEM_PRICE

total_with_vat = total_without_vat * (1 + VAT_PERCENTAGE)

if total_with_vat > 1000:
    discount = total_with_vat * 0.10
    total_with_vat -= discount

print("The total price is:", total_with_vat)
