# Enter an integer via the keyboard, for example, 9.
# Create a multiplication table as follows:


number = int(input("Enter the number: "))

for i in range(1, 21):
    print(i, "x", number, "=", i * number)
