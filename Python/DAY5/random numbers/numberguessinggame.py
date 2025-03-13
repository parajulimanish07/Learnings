#Python Number Guessing Game
import random

lowest_num = 1
highest_num = 99
answer = random.randint(lowest_num, highest_num) # Generate a random number between 1 and 99
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Guess the number: ")

    if guess.isdigit(): # Check if the input is a number
        guess = int(guess)
        guesses += 1 # Increment the number of attempts

        if guess < lowest_num or guess > highest_num:
            print("Number out of range!")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Too low!, Try again!")
        elif guess > answer:
            print("Too high!, Try again!")
        else:
            print(f"CORRECT! The number is {answer}!")
            print(f"Number of attempts: {guesses}")
            is_running = False

    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
