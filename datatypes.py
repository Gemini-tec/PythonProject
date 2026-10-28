age = 67 #integer
height = 3.25 #float
greeting = "Hello there" #string
isPythonInteresting = True #boolean


# Data Structures
cars = ["Ferrari", "Alfa Romeo", "Bugatti","Bentley","TrackHawk","Mercedes", "Maybach"] # List - Values are ordered and are changeable

fruits =  ( "Banana", "Mango", "Peaches") #Tuple - Ordered but unchangeable
countries = { "China", "France", "Germany", "Italy", "America"} #Set - Elements are unordered and unchangeable
# ASSIGNMENT
# Dictionary and an example - they store datain key:value pairs (Ordered, changeable and do no allow duplicates)
thisdict = {"brand":"Bugatti", "model": "chiron", "year":"1945"}
print(thisdict)
print(thisdict["year"])
print(thisdict["brand"])
# Arrays- special variable which can hold more than one value at a time
gari = ["BMW","Volkswagon", "lambo" ]
print(gari)
# typecasting - they give definite datatypes to values e.g.float,int,string
# Typecastig for integers
m = int(1.0)
n =int(40)
o = int("500")
print(m, n, o)
print(type(m), type(n), type(o)) # to indicate which datatype the item is
# Typecasting for floats
m = float(1.0)
n =float(40)
o = float("500")
print(m,n,o)
print(type(m),type(n),type(o))
# typecasting for strings
m = str(1.0)
n =str(40)
o = str("500")
print(m,n,o)
print(type(m),type(n),type(o))

# cars.append("Jetour")
# cars[0] = "Jaguar"
# print(cars, fruits,countries)
# print(isPythonInteresting, greeting, height,"is your height and ", age, "is your age")