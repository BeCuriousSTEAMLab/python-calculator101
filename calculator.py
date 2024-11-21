def calculator():
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid number")
        return
    
    operation = input("Enter operation (+, -, *, /): ")
    
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number")
        return
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operation")
        return
    
    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()