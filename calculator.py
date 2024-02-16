# Import the math module for mathematical functions
import math

# Define basic mathematical operations as functions
def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def addition(x, y):
    return x + y

def substraction(x, y):
    return x - y

# Define trigonometric functions using the math module
def cal_sinus(x):
    return math.sin(x)

def cal_cosinus(x):
    return math.cos(x)

def cal_tangent(x):
    return math.tan(x)

def cal_cotangent(x):
    return 1 / math.tan(x)

# Define inverse trigonometric functions using the math module
def cal_asin(x):
    return math.asin(x)

def cal_acos(x):
    return math.acos(x)

def cal_atan(x):
    return math.atan(x)

def cal_acotan(x):
    return 1 / math.atan(x)

# Define other mathematical functions using the math module
def cal_sqrt(x):
    return math.sqrt(x)

def cal_curt(x):
    calculation = math.pow(x, (1/3))
    return calculation

def cal_abs(x):
    return abs(x)

def cal_ln(x):
    return math.log(x)

def cal_log(x, bases):
    return math.log(x, bases)

def cal_exponential(x):
    return math.exp(x)

def cal_pow(x, y):
    calculation = pow(x, y)
    return calculation

# Main calculator function that handles different operations
def calculator(value1, operation, value2=None):
    if operation in ["sin", "cos", "tan", "cotan", "asin", "acos", "atan", "acotan",
                     "sqrt", "curt", "abs", "exp", "ln", "pow", "log"]:
        try:
            # Handling various mathematical functions
            if operation == "sin":
                value1 = cal_sinus(value1)
            elif operation == "cos":
                value1 = cal_cosinus(value1)
            elif operation == "tan":
                value1 = cal_tangent(value1)
            elif operation == "cotan":
                value1 = cal_cotangent(value1)
            elif operation == "asin":
                while not (-1 <= value1 <= 1):
                    print("Incorrect Value !!!")
                    value1 = float(input("Please enter a number between -1 annd 1 : "))
                else:
                    value1 = cal_asin(value1)
            elif operation == "acos":
                while not (-1 <= value1 <= 1):
                    print("Incorrect Value !!!")
                    value1 = float(input("Please enter a number between -1 and 1 : "))
                else:
                    value1 = cal_acos(value1)
            elif operation == "atan":
                value1 = cal_atan(value1)
            elif operation == "acotan":
                value1 = cal_acotan(value1)
            elif operation == "sqrt":
                while value1 < 0:
                    print("The square for negative number is not defined")
                    value1 = float(input("Please enter a positive number : "))
                else:
                    value1 = cal_sqrt(value1)
            elif operation == "curt":
                if value1 < 0:
                    raise ValueError("The cube root of a negative value is not defined ")
                value1 = cal_curt(value1)
            elif operation == "abs":
                value1 = cal_abs(value1)
            elif operation == "exp":
                value1 = cal_exponential(value1)
            elif operation == "pow":
                power = float(input("Enter your power :"))
                value1 = cal_pow(value1, power)
            elif operation == "ln":
                if value1 <= 0:
                    raise ValueError("The logarithm of zero or negative number is not defined")
                value1 = cal_ln(value1)
            elif operation == "log":
                base = float(input("Enter your logaritm base : "))
                if base <= 0 or base == 1 or value1 <= 0:
                    raise ValueError("Logarithm is not defined for this number")
                value1 = cal_log(value1, base)
        except ValueError as e1:  # here, 3 errors of the same type "ValuError". We managed one exception
            # and use a variable call valueerror to print the message error for each case
            print("Erreur :", e1)
        return value1
    else:
        try:
            # Handling basic arithmetic operations
            value2 = float(input("Enter a number : ")) if value2 is None else value2
            if operation == "x":
                if value1 == 0 or value2 == 0:
                    raise ValueError("cant multiply by zero")
                value1 = multiplication(value1, value2)
            elif operation == "/":
                if value2 == 0:
                    raise ZeroDivisionError("Division by zero is not defined")
                value1 = division(value1, value2)
            elif operation == "+":
                value1 = addition(value1, value2)
            elif operation == "-":
                value1 = substraction(value1, value2)
            else:
                print("Unknown operator")
                return value1
        except ZeroDivisionError as e2:
            # Handle division by zero error
            print("Error division :", e2)
            return value1
        except ValueError as e:
            # Handle value error for basic arithmetic operations
            print("Error multiplication :", e)
            return value1

        return value1

# User interface for the calculator
print()
print("Welcome to your calculator !!!")
print("Press x, /, +, - for multiplication, division, addition, substraction")
print("Press sin, cos, tan, cotan for sinus, cosinus, tangent, cotangent")
print("Press asin, acos, atan, acotan for arc sine, arc cosine, arc tangent, arc cotangent")
print("Press sqrt,curt,abs,for squareroot, cuberoot, absolute value")
print("Press exp, pow, for exponential, if you want to raise a number to power")
print("Press ln, log, for natural logarithm, logarithm with base")
print("Press exit if you finish")
print()

# Initialize result variable
result = 0

# Get the initial input from the user
while True:
    try:
        result = float(input("Enter a number : "))
        break
    except ValueError as e6:
        # Handle invalid input for the initial number
        print("Please enter a number !!!", e6)
        # The variable "error4" is used here to intercept the error and print the message.
        # in this case, the message error will be : could not convert string to float:
        continue

# Main loop for the calculator
while True:
    operator = input("Enter the operator or 'e' if you want to exit : ")
    if operator.lower() == "e":
        # Exit the calculator if the user inputs 'e'
        print("Goodbye !!!")
        break
    # Perform the calculation and display the result
    result = calculator(result, operator)
    print(result)
