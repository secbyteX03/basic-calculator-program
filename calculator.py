# Basic Calculator Program
# Get the first number from user
num1 = float(input("Enter the first number: "))
# Get the second number from user
num2 = float(input("Enter the second number: "))
# Get the operation from user
operation = input("Enter operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
#Handle invalid operations
else:
    print("Error: Invalid operation! Please use +, -, *, or /")
