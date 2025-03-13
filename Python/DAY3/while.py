#while loop = a statement that will execute its block of code as long as its condition is true\
#while condition chai loop ko condition true vaye samma chalxa else loop break huncha

num = int(input("Enter a number between 1 and 10: "))

while num <1 or num >10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10: "))


print(f"You number is {num}")