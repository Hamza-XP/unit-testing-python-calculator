import math
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored text
init(autoreset=True)

class CalculatorUI:
    def __init__(self):
        self.operations = {
            1: ("Addition", self.add),
            2: ("Subtraction", self.subtract),
            3: ("Multiplication", self.multiply),
            4: ("Division", self.divide),
            5: ("Square Root", self.square_root),
            6: ("Power", self.power),
            7: ("Modulus", self.modulus),
            8: ("Exit", None)
        }

    def display_header(self):
        print(Fore.CYAN + "\n" + "=" * 40)
        print(Fore.YELLOW + "✨ Scientific Calculator".center(40))
        print(Fore.CYAN + "=" * 40)

    def display_menu(self):
        print(Fore.GREEN + "\nMain Menu:")
        for key in sorted(self.operations.keys()):
            print(f"{Fore.MAGENTA}{key}. {self.operations[key][0]}")

    @staticmethod
    def get_input(prompt, color=Fore.WHITE):
        while True:
            try:
                return float(input(color + prompt + Style.RESET_ALL))
            except ValueError:
                print(Fore.RED + "Invalid input! Please enter a valid number.")

    def run(self):
        while True:
            self.display_header()
            self.display_menu()

            try:
                choice = int(self.get_input("\nEnter your choice (1-8): ", Fore.BLUE))
            except ValueError:
                print(Fore.RED + "Please enter a number between 1-8!")
                continue

            if choice == 8:
                print(Fore.YELLOW + "\nThank you for using the calculator! 👋")
                break

            if choice not in self.operations:
                print(Fore.RED + "Invalid choice! Please select 1-8")
                continue

            operation_name, func = self.operations[choice]
            self.perform_operation(operation_name, func)

    def perform_operation(self, name, func):
        print(Fore.CYAN + f"\n{' ' + name + ' ':-^40}")
        
        try:
            if func == self.square_root:
                num = self.get_input("Enter number: ")
                result = func(num)
                self.display_result(name, [num], result)
            else:
                num1 = self.get_input("Enter first number: ")
                num2 = self.get_input("Enter second number: ")
                result = func(num1, num2)
                self.display_result(name, [num1, num2], result)
        except ValueError as e:
            print(Fore.RED + f"\n⚠️ Error: {str(e)}")
        except Exception as e:
            print(Fore.RED + f"\n❌ Unexpected error: {str(e)}")

    def display_result(self, operation, inputs, result):
        print(Fore.GREEN + "\n" + "═" * 40)
        print(Fore.YELLOW + " RESULT ".center(40, "░"))
        if len(inputs) == 1:
            print(Fore.CYAN + f"{operation} of {inputs[0]:.4f} = {Fore.WHITE}{result:.6f}")
        else:
            print(Fore.CYAN + f"{inputs[0]:.4f} {operation.lower()} {inputs[1]:.4f} = {Fore.WHITE}{result:.6f}")
        print(Fore.GREEN + "═" * 40 + "\n")

    # Math operations
    @staticmethod
    def add(a, b): return a + b
    @staticmethod
    def subtract(a, b): return a - b
    @staticmethod
    def multiply(a, b): return a * b
    @staticmethod
    def divide(a, b):
        if b == 0: raise ValueError("Division by zero is not allowed")
        return a / b
    @staticmethod
    def square_root(a):
        if a < 0: raise ValueError("Square root of negative numbers is not real")
        return math.sqrt(a)
    @staticmethod
    def power(a, b): return a ** b
    @staticmethod
    def modulus(a, b):
        if b == 0: raise ValueError("Modulus by zero is undefined")
        return a % b

if __name__ == "__main__":
    CalculatorUI().run()