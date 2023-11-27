number = int(input("Enter the number: "))

index_1 = number % 10
index_2 = number % 100 // 10
index_3 = number // 100

print(f"The second-to-last digit is {index_2}")
print(f"The last digit is {index_1}")
print(index_3, index_1, index_2)
