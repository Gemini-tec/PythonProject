# Inheritance class polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!! \n")



class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!! \n")

class Plane(Vehicle):
    def move(self):
        print("Fly!! \n")

car1 = Car("Bugatti", "Chiron")
boat1 = Boat("Ibizza", "Erangel")
plane1 = plane = Plane("Boeing", "343")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()


# CLASS POLYMORPHISM
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!! \n")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!! \n")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!! ")

car1 = Car("Bugatti", "Chiron")
boat1 = Boat("Ibizza", "Erangel")
plane1 = Plane("Boeing", "747")


for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()


