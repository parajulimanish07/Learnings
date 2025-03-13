#Exercise 2 Shopping cart program

item=input("Enter the item you want to buy: ")
price=float(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity of the item: "))
total = price*quantity

print(f"You are buying {quantity} {item} at ${price} each")
print(f"Your total is ${total}")