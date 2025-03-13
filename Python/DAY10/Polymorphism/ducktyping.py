#"Duck typing" = A programming language feature that allows objects of different types to be used interchangeably wherever a specific type is required.
# Object must have the minimum necessary methods to perform the required operations.
# "If it looks like a duck and quacks like a duck, then it must be a duck."

class Animal:
    alive=True


class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

class Car:

    alive = True
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()] # This is not a Dog or Cat object, but it still works because it has a speak() method. It's a duck!]

for animal in animals:
    animal.speak()
    print(animal.alive) # This works because Animal class has a alive attribute. It's a duck!