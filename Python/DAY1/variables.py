# Variable = Container for a value(string, integer, float, boolean)
# String = A sequence of characters inside quotes
# Integer = A whole number
# Float = A number with a decimal point
# Boolean = True or False

# A variable behaves as if it is the value it contains.


#Strings
first_name = "John"
food="Burger"
email="manish@google.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#Integers
age = 23 #should not be in quotes as it is a number
quantity = 3.5 #float
num_of_students = 30 #integer

print(f"Your age is {age}")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#Float

price = 19.99
gpa = 3.9
distance = 5.5 

print(f"The price of the item is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")

#Boolean

is_student = False
for_sale = True
is_online = False

if is_online:
    print("You are online")
else:  
    print("You are offline")
if for_sale:
    print("The item is for sale")
else:
    print("The item is not for sale")



