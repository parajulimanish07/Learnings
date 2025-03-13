#class variables (shared among all instances of a class)
# defined outside the constructor (__init__ method)
#allow you to share data among all objects created from that class

class Student:

    class_year = 2027
    number_of_students = 0

    def __init__(self, name, age):  #self refers to the current object
        self.name = name  #instance variable
        self.age = age
        Student.number_of_students += 1  # increment the class variable for each new object created

student1 = Student("Manish", 20)
student2 = Student("Spongebob", 22)
student3 = Student("Patrick", 34)
student4 = Student("Squidward", 18)


print(f"My graduating class of {Student.class_year} has {Student.number_of_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)