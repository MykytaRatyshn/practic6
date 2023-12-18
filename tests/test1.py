import unittest
from app.calculator import Calculator

class TestCalculatorMethods(unittest.TestCase):
    def test_add(self):
        calc = Calculator(5, 3)
        self.assertEqual(calc.add(), 8)

        calc = Calculator(-2, 7)
        self.assertEqual(calc.add(), 5)

        # Additional tests
        calc = Calculator(0, 0)
        self.assertEqual(calc.add(), 0)

        calc = Calculator(-10, -5)
        self.assertEqual(calc.add(), -15)

    def test_subtract(self):
        calc = Calculator(10, 4)
        self.assertEqual(calc.subtract(), 6)

        calc = Calculator(3, 8)
        self.assertEqual(calc.subtract(), -5)

        # Additional tests
        calc = Calculator(0, 0)
        self.assertEqual(calc.subtract(), 0)

        calc = Calculator(-5, -10)
        self.assertEqual(calc.subtract(), 5)

    def test_multiply(self):
        calc = Calculator(6, 3)
        self.assertEqual(calc.multiply(), 18)

        calc = Calculator(-4, 5)
        self.assertEqual(calc.multiply(), -20)

        # Additional tests
        calc = Calculator(0, 5)
        self.assertEqual(calc.multiply(), 0)

        calc = Calculator(2, 0)
        self.assertEqual(calc.multiply(), 0)

    def test_divide(self):
        calc = Calculator(15, 3)
        self.assertEqual(calc.divide(), 5)

        calc = Calculator(7, 2)
        self.assertEqual(calc.divide(), 3.5)

        # Additional tests
        calc = Calculator(0, 5)
        self.assertEqual(calc.divide(), 0)

        calc = Calculator(10, 0)
        with self.assertRaises(ZeroDivisionError):
            calc.divide()

    def test_power(self):
        calc = Calculator(2, 3)
        self.assertEqual(calc.power(), 8)

        calc = Calculator(5, 0)
        self.assertEqual(calc.power(), 1)

        # Additional tests
        calc = Calculator(0, 5)
        self.assertEqual(calc.power(), 0)

        calc = Calculator(-2, 2)
        self.assertEqual(calc.power(), 4)

    def test_random_number(self):
        calc = Calculator(1, 10)
        random_num = calc.random_number(1, 10)
        self.assertTrue(1 <= random_num <= 10)

        calc = Calculator(-5, 5)
        random_num = calc.random_number(-5, 5)
        self.assertTrue(-5 <= random_num <= 5)

        # Additional tests
        calc = Calculator(0, 0)
        random_num = calc.random_number(0, 0)
        self.assertEqual(random_num, 0)

        calc = Calculator(-10, -5)
        random_num = calc.random_number(-10, -5)
        self.assertTrue(-10 <= random_num <= -5)

if __name__ == '__main__':
    unittest.main()
