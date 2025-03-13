#Slot machine program
import random
def spin_row():
    symbols = ['😍', '🍉', '⭐', '🍋', '🔔']

    return [random.choice(symbols) for _ in range(3)] # Spin a row of 3 symbols
def print_row(row):
    print("****************")
    print(" | ".join(row)) # Print the row of symbols, .join() is used to join the symbols in a row with a space
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '😍':
            return bet*10
        elif row[0] == '🍉':
            return bet *4
        elif row[0] == '🔔':
            return bet *5
        elif row[0] =='🍋':
             return bet * 6
        elif row[0] == '⭐':
            return bet * 20
    
    return 0

def main():
    balance = 100

    print("****************************")
    print("Welcome to the slot machine!")
    print("Symbols : 😍 🍉 ⭐ 🍋 🔔")
    print("****************************")

    while balance > 0:
        print (f"Your balance: ${balance}")

        bet = input("Place your bet amount : ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance :
            print("Insufficient funds. Please try again.")
            continue

        if bet <= 0:

            print("Bet amount must be greater than zero.")
            continue # Reset the balance to the initial amount

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout >0:
            print(f"Congratulations! You won ${payout}.")

        else:
            print("Sorry, you didn't win.")

        balance += payout


        play_again = input("Do you want to play again? (y/n) : ")
        
        if play_again.lower()!= 'y':
            break

    print(f"Thanks for playing!, Your final balance is ${balance}." )

if __name__ == "__main__":
    main()