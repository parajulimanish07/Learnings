#Inheritance = allows a class to inherit properties and methods from another class
# Helps with code reusability and maintainability and extensibilty of the code
# class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
# Child class inherits properties and methods from Animal class 
# We only have to write the specific implementation for the new class

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog= Dog("Pogo")
cat= Cat("Milley")
mouse= Mouse("Bhuntey")

print(dog.name)
print(dog.is_alive)

dog.eat()
dog.sleep()
dog.speak()