# Static methods = belong to the class itself, not an instance of the class
# Usually used for general utility functions that do not need access to instance data

#Instance methods = Best for operations on instances of the class (objects)
#Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"        
    
    @staticmethod # static method is defined using the @staticmethod decorator 

    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("John Doe", "Manager")
employee2 = Employee("Jane Smith", "Cashier")
employee3 = Employee("Mike Johnson", "Janitor")

print(Employee.is_valid_position("Baller")) # static method can be called directly on the class itself
print(employee1.get_info()) # instance method can be called on an instance of the class
print(employee2.get_info()) 
print(employee3.get_info()) 
