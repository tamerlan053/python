Problem

# Write a Python program that calculates and displays the first n numbers in the Fibonacci sequence. 
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 
# Your task is to prompt the user for the number of terms they wish to calculate and then display those terms.

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    num_terms = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
    if num_terms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        print(fibonacci(num_terms))

if __name__ == "__main__":
    main()
