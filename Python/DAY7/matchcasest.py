#Match case statement (switch) : An alternative to if-elif-else statements
# Execute some code if a value matches a certain condition
#Benefits: Code is cleaner, easier to read, and less error-prone

# Example 1

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _: #Wilcard case to handle any other values, if not matched with any other case 
            return False
        
print(is_weekend("Sunday")) # Output: Monday
