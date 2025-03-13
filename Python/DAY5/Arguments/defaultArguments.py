#default arguments = Arguments that have a default value 
#                     default is used when the argument is not provided in the function call
#                    make your function more flexible and easier to use 
# 1. positional arguments: they must be provided in the correct order
# 2. Default arguments: they can be provided in any order
# 3. keyword arguments: they can be provided in any order, and they must be preceded by an argument name
# 4. arbitrary arguments: *args and **kwargs are used to handle variable number of arguments

#DEFAULT arguments example

#def net_price(list_prices, discount=0, tax=0.05): # default discount is 0 and tax is 5%
 #   return list_prices * (1 - discount) * (1 + tax)

#print(net_price(500))
#print(net_price(500, 0.1)) # discount is 10%

#print(net_price(500, 0.1, 0)) # discount is 10%


#Example 2

import time

def count(end, start=0):
    for x in range(start, end+1): # range function le 0 bata end samma ko range banako
        print(x)
        time.sleep(1) # sleep for 1 second ani loop continue huncha
    print("DONE!")

count(30,15)
