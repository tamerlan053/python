number = float(input("Enter a floating-point number: "))

digit_after_decimal = int((number * 10) % 10)

print(f"Digit after the decimal point: {digit_after_decimal}")
