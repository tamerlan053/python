# Exercise 2

# Write a function that returns whether a given year is a leap year or not. 
# A leap year is divisible by 4, but not divisible by 100. 
# If the year is divisible by 400, it is again a leap year. Make sure the result is a boolean.

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def main():
    year = int(input("Enter the year: "))
    output = is_leap_year(year)
    print("Is this a leap year?", output)

if __name__ == '__main__':
    main()
