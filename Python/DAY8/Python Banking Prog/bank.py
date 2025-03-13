# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f} dollars")

def deposit():
    amount = float(input("Enter the amount to deposit: "))


    if amount < 0 :
        print("Invalid amount! Please enter a positive value.")
        return 0
    else:
        return amount



def withdraw(balance):
    amount = float(input ('Enter the amount to withdraw: '))

    if amount > balance :
        print("Insufficient balance! You can't withdraw that amount.")
        return 0
    elif amount < 0 :
        print("Invalid amount! Please enter a positive value.")
        return 0
    else:
        return amount    

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("  Welcome to Banking System   ")
        print("*******************")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*******************")
            print("Invalid choice! Please try again.")
            print("*******************")

    print("*******************")
    print("Thank you for using our banking system, Have a nice day!")
    print("*******************")



if __name__ == '__main__':
    main()