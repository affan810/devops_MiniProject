import math
import logging
import sys

#set up logging to write to calculator.log
logging.basicConfig(filename="calculator.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def square_root(x):
    result = math.sqrt(x)
    logging.info(f"Calculated square root of {x}: {result}")
    return result

def factorial(x):
    result = math.factorial(x)
    logging.info(f"Calculated factorial of {x}: {result}")
    return result

def power(x, exponent):
    result = math.pow(x, exponent)
    logging.info(f"Calculated {x} raised to the power of {exponent}: {result}")
    return result

def natural_log(x):
    result = math.log(x)
    logging.info(f"Calculated natural logarithm of {x}: {result}")
    return result

def main():
    while True:
        print("Select operation:")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Power")
        print("4. Natural Logarithm")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator.")
            logging.info("Calculator exited by user.")
            sys.exit()
        try:
            if choice == '1':
                num = float(input("Enter a number: "))
                print(f"Square root of {num} is {square_root(num)}")
            elif choice == '2':
                num = int(input("Enter a non-negative integer: "))
                print(f"Factorial of {num} is {factorial(num)}")
            elif choice == '3':
                base = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent: "))
                print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
            elif choice == '4':
                num = float(input("Enter a number: "))
                print(f"Natural logarithm of {num} is {natural_log(num)}")
            else:
                print("Invalid input. Please try again.")
                logging.warning("Invalid menu choice entered.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            logging.error("Invalid input encountered.")

if __name__ == "__main__":
    main()