import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    
    player = None
    computer = random.choice(options)

    
    while player not in options:
        player = input ("Enter a valid choice (rock, paper, scissors): ")
        

    print(f"Player chose: {player}")

    print(f"Computer chose: {computer}")

    if player == computer:
        print("Its a tie!")

    elif player == "rock" and computer == "scissors":
        print("You win!")

    elif player =="paper" and computer == "rock":
        print("You win")

    elif player == "scissors" and computer == "paper":
        print("You win!")

    else: 
        print("Computer wins!")
        
    if not input("Do you want to play again? (yes/no): ").lower() == "yes":
        playing = False

print("Thanks for playing!")

