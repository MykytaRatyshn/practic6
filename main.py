from app.calculator import Calculator

def main():
   a = int(input("Enter a: "))
   b = int(input("Enter b: "))
   calc = Calculator(a, b)
   print(f"{a} + {b} = ", calc.add())
   print(f"{a} - {b} = ", calc.subtract())
   print(f"{a} * {b} = ", calc.multiply())
   print(f"{a} / {b} = ", calc.divide())
   print(f"{a} ^ {b} = ", calc.power())
   print(f"Random number in the range from {a} to {b}:", Calculator.random_number(a, b))
if __name__ == "__main__":
   main()



