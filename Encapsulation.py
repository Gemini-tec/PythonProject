# read and do research...creating a sample program
# ENCAPSULATIION -  All about protecting data inside a class

class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #you create a private property using __

    def get_age(self): #we use getters to access private properties value
        return self.__age
p1 = person("Jane Kariuki", 20)
print(p1.name)
print(p1.get_age())


# using setters to changge the value of private properties
class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age CANNOT be a -Ve number")

p1 = person("John Kamadi", 22)
print(p1.name)
print(p1.get_age())

p1.set_age(12)
print(p1.get_age())
