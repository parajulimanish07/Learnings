#condition expression =  A one-line shortcut for an if-else statement (a ternary operator)
# Print or assign one of two values based on a condition
# X if condition else Y

num = 5
a = 6 
b = 7 
age = 25
temperture = 30
user_role = "guest"

# print("Positive" if num>0 else "Negative") 

# result = "Even" if num%2 == 0 else "Odd"

# min_num = a if a < b else b

# status = "Adult" if age >= 18 else "Child"

# weather = "Hot" if temperture >= 30 else "Cold"

access_level = "Full Access" if user_role == "admin" else "Limited Access"

print (access_level)