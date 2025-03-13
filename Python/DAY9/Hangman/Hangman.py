#Hangman in python

from wordslist import words
import random


#dictionary of key:()
hangman_art ={0:("     ",
                 "     ",
                 "     "),
              1:("  o  ",
                 "     ",
                 "     "),
              2:("  o  ",
                 "  |  ",
                 "     "),
              3:("  o  ",
                 "/ |  ",
                 "     "),
              4:("  o  ",
                 "/ |\\",
                 "     "),
              5:("  o  ",
                 "/ |\\",
                 " /    "),
              6:("  o  ",
                 "/ |\\",
                 " / \\")}

def display_man(wrong_guesses):
    print("**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************")
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer) #hint array with underscores, len(answer) is the length of the answer
    wrong_guesses = 0
    guessed_letters = set() #set to store already guessed letters
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint) #display the hint array with the guessed letter
        guess = input("Guess a letter: ").lower()

        if len(guess)!= 1 or not guess.isalpha(): #check if the guess is a single letter and is alphabetic
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"{guess} has already been guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)): #replace the underscore in the hint array with the correct letter
                if answer[i] == guess:
                    hint[i] = guess  # Corrected the assignment operator
        else:
            wrong_guesses += 1


        if "_" not in hint: #check if all the letters have been guessed correctly
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You guessed the word.")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:  # Changed the condition to >=
            display_man(wrong_guesses)
            display_answer(answer)
            print("Game Over! You lost.")
            is_running = False

if __name__ == "__main__": #run the program only if it's being run directly #Dunged the line to fix the bug
    main()