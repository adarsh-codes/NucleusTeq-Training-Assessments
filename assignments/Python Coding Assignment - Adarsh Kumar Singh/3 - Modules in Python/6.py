import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

parser = argparse.ArgumentParser(description="Simple CLI Calculator")

parser.add_argument("a", type=float, help="First number")
parser.add_argument("b", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")

args = parser.parse_args()

if args.operation == "add":
    result = add(args.a, args.b)
elif args.operation == "sub":
    result = subtract(args.a, args.b)
elif args.operation == "mul":
    result = multiply(args.a, args.b)
elif args.operation == "div":
    result = divide(args.a, args.b)

print(f"Result: {result}")
