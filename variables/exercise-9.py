amount = int(input("Enter the amount in cents: "))

euros2 = amount // 200
amount = amount % 200

euros1 = amount // 100
amount = amount % 100

cents50 = amount // 50
amount = amount % 50

cents20 = amount // 20
amount = amount % 20

cents10 = amount // 10
amount = amount % 10

cents5 = amount // 5
amount = amount % 5

cents2 = amount // 2
amount = amount % 2

cents1 = amount

print("The amount is:", euros2, "of 2 euros;", euros1, "of 1 euro;", cents50, "of 50 cents;", cents20, "of 20 cents;", cents10, "of 10 cents;", cents5, "of 5 cents;", cents2, "of 2 cents;", cents1, "of 1 cent;")
