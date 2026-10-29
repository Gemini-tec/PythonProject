# Parent Class/ SUPER CLASS/ Base class
class Animal:
    ismammal = True
    age = 3

    def movement(self):
        print("Animal is moving")


# Child Class/ Sub class / derived class
class Dog(Animal): #inheritance

    def bark(self):
        print("woof!! woof!! woof!! \n")

class Cat(Animal):

    def meow(self):
        print("meow!! meow!! moew!!")

dog1 = Dog()
dog1.movement()
dog1.bark()
print(dog1.age, dog1.ismammal)

cat1 = Cat()
cat1.meow()