def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {result}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {result}")

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    calculator()
