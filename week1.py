

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

# Perform calculation
if operation == "add":
    result = num1 + num2
    print("Result:", result)
elif operation == "subtract":
    result = num1 - num2
    print("Result:", result)
elif operation == "multiply":
    result = num1 * num2
    print("Result:", result)
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation.")
