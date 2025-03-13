#Class methods = Allow operations related to the class itself
# Take (cls) as the first argument and represents class itself, not an instance of the class

#Instance method = Best for operations related to an instance of the class(objects)
#Static method = Best for utility functions that do not need access to class data
#Class methods = Best for class-level data or require access to the class itself

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += self.gpa

#INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod # class method is defined using the @classmethod decorator
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"

student1 = Student("Manish Parajuli", 3.8)
student2 = Student("SpongeBob SquarePants", 3.6)
student3 = Student("Patrick Star", 3.9)

print(Student.get_count())

print(Student.get_average_gpa())