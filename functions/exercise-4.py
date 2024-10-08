# Exercise 4

# A random integer is generated between 1 and 10 (inclusive), and the user is allowed to try to guess it.
# The computer provides feedback: "higher," "lower," or "congratulations, number guessed." 
# Use a function to provide the feedback. The player can only guess 4 times! 
# The game stops if the number is guessed or if the 4 attempts are over.

import random

def generate_random():
    return random.randint(1, 10)

def give_feedback(input_number, random_number):
    if input_number < random_number:
        return "higher"
    elif input_number > random_number:
        return "lower"
    else:
        return "congratulations, the number has been guessed"

def main():
    random_number = generate_random()
    counter = 0

    while counter < 4:
        input_number = int(input("Enter a number: "))

        if input_number == random_number:
            print("Congratulations, the number has been guessed")
            return

        print(give_feedback(input_number, random_number))
        counter += 1

    print("Your 4 attempts are over")

if __name__ == '__main__':
    main()
