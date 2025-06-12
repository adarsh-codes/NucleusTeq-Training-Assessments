try:
    result = 2/0
    print(result)
except ZeroDivisionError:
    print("Division by zero!!")
finally:
    print("Python Assignment.")