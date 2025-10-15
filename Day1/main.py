from calculator import Calculator
from exceptions import CalculatorError

def main():
    calc = Calculator()
    
    print("=== Welcome to Python Stream Calculator ===")
    
    while True:
        print("\nSelect operation: add, subtract, multiply, divide, stream or exit")
        op = input("Operation: ").strip().lower()
        
        if op == "exit":
            print("Exiting calculator. Goodbye!")
            break
        
        try:
            if op == "stream":
                numbers = input("Enter numbers separated by space: ")
                numbers = [float(x) for x in numbers.split()]
                operation = input("Choose operation: add, subtract, multiply, divide: ").strip().lower()
                print(f"Streaming {operation} results:")
                for result in calc.stream_operations(operation, numbers):
                    print(result)
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                
                if op == "add":
                    print("Result:", calc.add(a, b))
                elif op == "subtract":
                    print("Result:", calc.subtract(a, b))
                elif op == "multiply":
                    print("Result:", calc.multiply(a, b))
                elif op == "divide":
                    print("Result:", calc.divide(a, b))
                else:
                    raise CalculatorError(f"Invalid operation: {op}")
        except CalculatorError as e:
            print("Calculator Error:", e)
        except ValueError:
            print("Please enter valid numbers.")
        except Exception as e:
            print("Unexpected Error:", e)

if __name__ == "__main__":
    main()
