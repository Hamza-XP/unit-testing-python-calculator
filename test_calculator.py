# test_calculator.py
import unittest
import colorama
from colorama import Fore, Style
from calculator import CalculatorUI

# Initialize colorama for test output formatting
colorama.init(autoreset=True)

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n" + "="*60)
        print(f"{Fore.CYAN}Starting Test Suite{Style.RESET_ALL}".center(60))
        print("="*60 + "\n")

    def setUp(self):
        self.calc = CalculatorUI()
        print(f"\n{Fore.MAGENTA}{'-'*40}")
        print(f"{Fore.BLUE}Running test: {self._testMethodName}")
        print(f"{Fore.MAGENTA}{'-'*40}{Style.RESET_ALL}")

    # Test cases with color-formatted output
    def test_addition(self):
        """Test various addition scenarios"""
        print(f"{Fore.WHITE}Testing addition of various number combinations")
        self.assertEqual(self.calc.add(2, 3), 5, "Positive integers failed")
        self.assertEqual(self.calc.add(-1, -1), -2, "Negative integers failed")
        self.assertEqual(self.calc.add(0, 5), 5, "Zero addition failed")
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0, "Floats addition failed")
        print(f"{Fore.GREEN}✓ Addition test passed")

    def test_division_by_zero(self):
        """Test division by zero protection"""
        print(f"{Fore.WHITE}Testing division by zero protection")
        with self.assertRaises(ValueError, msg="Division by zero failed to raise error"):
            self.calc.divide(10, 0)
        print(f"{Fore.GREEN}✓ Division by zero protection works")

    def test_square_root_negative(self):
        """Test negative square root handling"""
        print(f"{Fore.WHITE}Testing square root of negative numbers")
        with self.assertRaises(ValueError, msg="Negative sqrt failed to raise error"):
            self.calc.square_root(-4)
        print(f"{Fore.GREEN}✓ Negative sqrt protection works")

    def test_modulus_operation(self):
        """Test modulus operations"""
        print(f"{Fore.WHITE}Testing modulus operations")
        self.assertEqual(self.calc.modulus(10, 3), 1, "Positive modulus failed")
        self.assertEqual(self.calc.modulus(-10, 3), 2, "Negative dividend failed")
        print(f"{Fore.GREEN}✓ Modulus operations correct")

    def test_power_operations(self):
        """Test power function scenarios"""
        print(f"{Fore.WHITE}Testing various power scenarios")
        self.assertEqual(self.calc.power(2, 3), 8, "Positive exponents failed")
        self.assertEqual(self.calc.power(5, 0), 1, "Zero exponent failed")
        self.assertAlmostEqual(self.calc.power(10, -1), 0.1, delta=0.001,
                             msg="Negative exponents failed")
        print(f"{Fore.GREEN}✓ Power operations validated")

    def tearDown(self):
        print(f"{Fore.YELLOW}Completed: {self._testMethodName}")
        print(f"{'='*40}\n{Style.RESET_ALL}")

    @classmethod
    def tearDownClass(cls):
        print("\n" + "="*60)
        print(f"{Fore.CYAN}Test Suite Completed{Style.RESET_ALL}".center(60))
        print("="*60)

if __name__ == "__main__":
    unittest.main(verbosity=2)