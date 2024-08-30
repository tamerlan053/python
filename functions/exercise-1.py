# Exercise 1

# A bank clerk wants to quickly calculate the value of a certain amount in euros in US dollars. 
# At the beginning of the program, he enters the value of the euro against the US dollar, for example, 1 euro = 1.072 US dollars (1.072 is entered). 
# Subsequently, amounts in euros are entered, after which the value in US dollars is displayed. 
# The conversion takes place via a function. The program ends when 0 is entered for the amount in euros.

def convert(rate, amount):
    value = rate * amount
    return value

def main():
    exchange_rate = float(input("Enter exchange rate: "))
    amount = int(input("Enter the amount to convert in euros: "))

    while amount != 0:
        total = convert(exchange_rate, amount)

        print("Amount in dollars is", total)

        amount = int(input("Enter the amount to convert in euros: "))

if __name__ == '__main__':
    main()
