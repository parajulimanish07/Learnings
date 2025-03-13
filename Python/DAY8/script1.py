# if __name__ == "__main__": # This will prevent the code from running when imported as a module
# Good pracitce (code is modular and can be reused) 



def favorite_food(food):
    print(f"My favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("Pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()