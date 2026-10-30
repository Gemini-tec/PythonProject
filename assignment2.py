
print("SIMPLE CALCULATOR")
print("Select an Operation")
print("1. Add (+)")
print("2. Subraction (-)")
print("3. Multiply (*)")
print("4. Division (/)")

choice = input("Select an operation (1,2,3,4): ")

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

if choice == 1:
    results = num1 +num2
    print(results)
if choice == 2:
    results = num1 - num2
    print(results)
if choice == 3:
    results = num1 * num2
    print(results)
if choice == 4:
    if num2 == 0:
        print("CANNOT DIVIDE BY ZERO !!")
    else:
        results = num1 / num2
        print(results)
else:
    print("INVALID CHOICE!!")

