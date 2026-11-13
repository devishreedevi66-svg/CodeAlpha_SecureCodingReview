# Secure Calculator

print("Secure Calculator")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
            result = None
        else:
            result = num1 / num2

    else:
        print("Invalid operator")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers.")