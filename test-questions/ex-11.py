# Exercise 11

# Write a Python program to count the number of vowels in a given string. 
# The string should be input by the user. 
# The program should display the total count of vowels (both uppercase and lowercase) and the count of each individual vowel.

def count_vowels(s):
    vowels = 'aeiou'
    count = {v: 0 for v in vowels}
    # Total vowels counter
    total_vowels = 0

    for char in s.lower():
        if char in vowels:
            count[char] += 1
            total_vowels += 1

    return count, total_vowels

def main():
    user_input = input("Enter a string to count vowels: ")
    vowels_count, total = count_vowels(user_input)
    print("Total vowels:", total)
    print("Count of each vowel:")
    for vowel, c in vowels_count.items():
        print(f"{vowel}: {c}")

if __name__ == "__main__":
    main()
