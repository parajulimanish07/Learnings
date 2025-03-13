#membership operators = checks if a value is present in a sequence (list, tuple, set, dictionary)
# 1. in= checks if a value is present in a sequence 2. not in= checks if a value is not present in a sequence

email = "example@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else :
    print("Invalid email")