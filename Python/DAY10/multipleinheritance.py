 #multiple inheritance = A class that inherits from more than one parent class
# C(A,B) - subclass C that inherits from classes A and B

#multilevel inheritance = A class that can inherit from a parent which inherits from another parent
# C(B) <- B(A) <- A
#hajurbuwa ko characteristics pani nati le inherit garna payo


class Animal:

    def __init__(self, name): #constructor method (runs automatically when an object is created), dunder method
        self.name = name
        
    def eat(self):
        print(f"{self.name} eats")
    def sleep(self):
        print(f"{self.name} sleeps")
    

class Prey(Animal):
    def flee(self):
        print(f"{self.name} flees")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} hunts")

class Rabbit(Prey):
    pass    

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nimo")

hawk.sleep()