# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take user input for operation
    choice = input("Enter choice (1/2/3/4): ")

    # Validate choice
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return

    # Take user input for numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Perform calculation based on user choice
    if choice == '1':
        print(f"The result of addition: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of subtraction: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of multiplication: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of division: {divide(num1, num2)}")

# Run the calculator
if __name__ == "__main__":
    main()
