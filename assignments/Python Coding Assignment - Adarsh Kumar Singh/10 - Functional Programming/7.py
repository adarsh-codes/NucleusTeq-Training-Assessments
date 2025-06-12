import functools

number = int(input("Enter a number to calculate factorial: "))

if number == 0:
    result = 1
else:
    result = functools.reduce(lambda x, y: x * y, range(1, number + 1))

print(f"Factorial of {number} is: {result}")
