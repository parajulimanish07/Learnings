#polymorphism - many forms or faces, Greek, "poly" means many, "morphos" means forms
#Two ways to achieve polymorphism:
# 1. Inheritance: an object could be treated of the same way as a parent class
# 2. "Duck typing": Object must have necessary attributes and methods. This approach is more flexible and doesn't require a class hierarchy.

from abc import ABC, abstractmethod # Abstract Base Classes (ABCs)


class Shape:
    
    @abstractmethod #This method must be implemented by subclasses, otherwise it will raise an error 
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius): #self is the instance of the class, radius is an instance variable
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2  # area of a square is side^2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height    

    def area(self):
        return 0.5 * self.base * self.height  # area of a triangle is 0.5 * base * height

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)  # call the parent class's constructor
        self.topping = topping
        self.radius = radius    

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]


for shape in shapes:
    print(f"{shape.area()}cm^2") # calling area method of each shape object, which will return the correct area for each shape