# Class is a blueprint of an object
# Object is an instance of a class

class Employee:

    def __init__(self, name, gender, position, age):
        self.name = name
        self.gender = gender
        self.position = position
        self.age = age


    def drive(self):
        print("Employee is Driving")

    def eat(self):
        print("Employee is Eating")




employee1 = Employee("John", "Male", "Managing Director", 67) # creating an object
print(employee1.name, employee1.gender, employee1.position, employee1.age)
employee1.drive()
employee1.eat()

employee2 = Employee("Jane", "Female", "Admin", 38)
print(employee2.name, employee2.gender, employee2.position, employee2.age)
employee2.drive()
employee2.eat()

employee3 = Employee("Doris", "Female", "CSO", 26)
print(employee3.name, employee3.gender, employee3.position, employee3.age)
employee3.eat()
employee3.drive()