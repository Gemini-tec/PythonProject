# Simple Calculator

print("Select an Operation: ")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (* )")
print("4. Divide (/ )")

choice = input("Enter your choice: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    results = num1 + num2
    print(results)
elif choice == "2":
    results = num1 - num2
    print(results)
elif choice == "3":
    results = num1 * num2
    print(results)
elif choice == "4":
    if num2 == 0:
        print("Cannot Divide by zero4")
    else:
        results = num1 / num2
        print(results)
else:
    print("Invalid choice")
