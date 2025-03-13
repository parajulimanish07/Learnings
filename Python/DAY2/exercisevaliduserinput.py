#exercise1

# validate user input exercise 
# 1. username is no more than 12 characters long
# 2. username must not contain space
# 3. username must not contain digits

username = input("Enter your username: ")


username.find(" ")


if len(username) > 12:
    print("your username cant be more than 12 characters")

elif not username.find(" ") == -1: # -1 means no space found in the string
    print("your username cant contain space")

elif not username.isalpha():
    print("your username cant contain digits")
    
else:
    print(f"Welcome {username}")