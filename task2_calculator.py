"""Task 2: Simple Calculator."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
    return None


def main():
    print("===== SIMPLE CALCULATOR =====")
    while True:
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        print("\nOperations: + (add)  - (subtract)  * (multiply)  / (divide)")
        op = input("Choose an operation: ").strip()

        result = calculate(a, b, op)
        if result is None:
            print("Invalid operation. Please use +, -, * or /.")
        else:
            print(f"\nResult: {a} {op} {b} = {result}")

        again = input("\nDo another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the calculator!")
            break
        print()


if __name__ == "__main__":
    main()
