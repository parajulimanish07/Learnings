#nested loop = A loop inside another loop (outer loop and inner loop)
#            outer loop:
#                 inner loop:

rows = int(input("Enter the number of rows: ")) 
columns = int(input("Enter the number of columns: ")) 
symbol = input("Enter a symbol to use: ")

for x in range(rows): # outer loop range 3 vayo so 3 patak inner loop run huncha
    for y in range(columns): 
        print(symbol, end="") # end="" le print statement ko output lai ek line ma display garna help garxa
    print() # inner loop ko output lai ek line ma display garna ko lagi print() use gareko ho



