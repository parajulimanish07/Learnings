# object = bundle of related attributes (variables) and methods (functions)
# Ex. phone, cup, book
# You need a "class" to create many objects

# class = blueprint for creating objects
class Car:
    def __init__(self, model, year, color, for_sale):  # constructor method (runs automatically when an object is created), dunder method
        self.model = model  # instance variable
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}!")

    def stop(self):
        print(f"You stop the {self.color}{self.model}.")

    def describe(self):
        print(f"{self.year} {self.color} {self.model} is {'for sale' if self.for_sale else 'not for sale'}.")