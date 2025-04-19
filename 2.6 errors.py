def main():
    try:
        num1 = get_number("Enter first number: ")
        
        operation = input("Enter operation (+, -, *, /, **): ")
        if operation not in ["+", "-", "*", "/", "**"]:
            raise ValueError("Invalid operation")
        
        num2 = get_number("Enter second number: ")
        
        result = calculate(num1, operation, num2)
        print(f"Result: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except KeyboardInterrupt:
        print("\nCalculator terminated.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid number.")
        return get_number(prompt)

def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError
        return num1 / num2
    elif operation == "**":
        return num1 ** num2

if __name__ == "__main__":
    main()