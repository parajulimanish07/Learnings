#Shopping cart program
#lists, sets and tuples

foods = [] #tuples are unchangeable and sets are unordered so we use list
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) :")
    if food.lower() == 'q': #food.lower() converts the input to lowercase temporarily
        break
    else:
        price = float(input(f"Enter the price of {food} : $"))
        foods.append(food) #append adds the input to the list
        prices.append(price) 

print("------YOUR CART------")

for food in foods:
    print(food, end=" ") #end=" " prints the output in the same line

for price in prices:
    total += price

print() #prints a blank line
print(f"Your total is : ${total}")