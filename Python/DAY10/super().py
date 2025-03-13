#super() = It allows us to refer to the parent class from the child class.
# function used in a child class to call methods from a parent class(superclass)
#Allows you to extend the functionality of the inherited methods.


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)  # calling the constructor of parent class (Shape)
        self.radius = radius

    def describe(self):
        super().describe()  # calling the overridden method from parent class (Shape)
        print(f"It is a circle with an area of {3.14 * self.radius ** 2} cm^2")  #Method overriding 

class Square(Shape):
     def __init__(self, color, filled, width):
        super().__init__(color, filled)  
        self.width = width

        super().describe()  # calling the overridden method from parent class (Shape)
        print(f"It is a square with an area of {self.width * self.width} cm^2")  #Method overriding 

class Triangle(Shape):
     def __init__(self, color, filled, width, height):
        super().__init__(color, filled)  
        self.width = width
        self.height = height

        super().describe()  # calling the overridden method from parent class (Shape)
        print(f"It is a traingle with an area of {self.width * self.height / 2} cm^2")  #Method overriding 

circle = Circle("red", True, 5)
square = Square("blue", False, 10)
triangle = Triangle("green", True, 8, 6)

circle.describe()

#we dont need to call the constructor of parent class manually in the child class, it automatically gets called.
#We can reuse the constructor of parent class by using super() function.