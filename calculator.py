def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    try:
        if choice == "1":
            result = add(x, y)
            operation = "+"
        elif choice == "2":
            result = subtract(x, y)
            operation = "-"
        elif choice == "3":
            result = multiply(x, y)
            operation = "*"
        elif choice == "4":
            result = divide(x, y)
            operation = "/"
        else:
            print("Invalid choice.")
            return

        print(f"{x} {operation} {y} = {result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
