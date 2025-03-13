#function = A block of reusable code that performs a specific task
# it takes some input, performs a computation, and produces some output
#place () after function name to call the function

def happy_birthday(name,age):  #def = define a function #order matters: name, age should be provided as arguments when calling the function
    print(f"Happy birthday to {name}!")  #print = print the message
    print(f"You are {age} years old!")
    print("You deserve a cookie!")
    print()


happy_birthday("Manish", 23)  #call the function
happy_birthday("John", 20)  
happy_birthday("Sarah", 30)  