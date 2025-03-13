#format specifiers in python are used to format the output of the program in a more readable form.


price1 = 3141.5
price2 = -99.99
price3 = 121212.3334

print(f"Price 1 is ${price1:.1f}") #f is for float, .2f is for 2 decimal places
print(f"Price 2 is ${price2:010}") #010 is for 10 spaces
print(f"Price 3 is ${price3:10}") #10 is for 10 spaces

print(f"Price 1 is ${price1:<10}") #< is for left align
print(f"Price 2 is ${price2:>10}") #> is for right align
print(f"Price 3 is ${price3:^10}") #^ is for center align

print(f"Price 1 is ${price1:+}") #+ is for positive sign
print(f"Price 2 is ${price2: }") #space is for positive sign
print(f"Price 3 is ${price3:+,.2f}") #, is for comma separator, .2f is for 2 decimal places and + is for positive sign

print(f"Price 1 is ${price1:,}") #, is for comma separator



