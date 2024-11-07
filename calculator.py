class Operation:
    """Base class for all operations."""

    def calculate(self, a, b=None):
        raise NotImplementedError("This method should be overridden by subclasses.")

class Addition(Operation):
    def calculate(self, a, b):
        return a + b

class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b

class Multiplication(Operation):
    def calculate(self, a, b):
        return a * b

class Division(Operation):
    def calculate(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

class Square(Operation):
    def calculate(self, a):
        return a * a

class SquareRoot(Operation):
    def calculate(self, a):
        if a < 0:
            return "Error: Cannot compute square root of negative number"
        return a ** 0.5

class Power(Operation):
    def calculate(self, a, b):
        return a ** b


class Calculator:
    def __init__(self):
        self.operations = {
            '1': Addition(),
            '2': Subtraction(),
            '3': Multiplication(),
            '4': Division(),
            '5': Square(),
            '6': SquareRoot(),
            '7': Power()
        }

    def display_menu(self):
        print("\nBasic Calculator")
        print("\n===================")
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Square Root")
        print("7. Power")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")

            if choice == '8':
                print("Exiting the calculator.")
                break

            if choice in self.operations:
                if choice in ['1', '2', '3', '4', '7']:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    result = self.operations[choice].calculate(a, b)
                elif choice in ['5', '6']:
                    a = float(input("Enter number: "))
                    result = self.operations[choice].calculate(a)
                else:
                    print("Invalid choice. Please try again.")
                    continue

                print(f"Result: {result}")
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
