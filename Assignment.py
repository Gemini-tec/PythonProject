# Largest among Three
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter Third number: "))

# Method 1
if a >= b and a >=c :
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# print(largest)
print(f"largest number is: {largest}")

# method 2
largest = max(a,b,c)
print(f"largest number is: {largest}")



