#Concession stand program

#dictionary {key:value}

menu = {"momo" : 3.00,
        "nachos" : 2.00,
        "fries" : 1.50,
        "popcorn" : 5.00,
        "soda" : 3.5}

cart = []
total = 0

print("---------MENU---------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}") #10 le 10 spaces diyo

print("---------------------")

while True:
    food = input("Select an item (q to quit) :").lower()
    if food == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)

print("---------YOUR ORDER-----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")