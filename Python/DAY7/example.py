#module = a file containing Python code that can be imported and used in other programs
# use 'import' keyword to import a module
# useful to break down large programs into smaller, more manageable parts

#import math 
# import math as m
#from math import e, sqrt, pi

pi = 3.14159

def square(x):
    return x ** 2 # function to calculate square of a number
def cube(x):
    return x ** 3 # function to calculate cube of a number

def circumference_of_circle(radius):
    return 2 * pi * radius # function to calculate circumference of a circle

def area(radius):
    return pi * radius ** 2 # function to calculate area of a circle