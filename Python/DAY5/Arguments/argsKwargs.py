# *args = allows you to pass multiple non-keyworded arguments to a function
# **kwargs = allows you to pass multiple keyworded arguments to a function
# *unpacking operator is used to unpack the arguments into individual variables
# 1. positional 2.default 3.keyword 4.ARBITARY


# *args example

# def display_name(*args):
#    for arg in args:
#        print(arg, end=" ")

# display_name("Manish", "Singh", "Kumar")


# **kwargs example

def print_address(**kwargs):
    for key,value in kwargs.items(): #unpacking key and values into individual variables
        print(f"{key} : {value}")


print_address(street="123 Main St",city="New York",state="NY", apt="100")