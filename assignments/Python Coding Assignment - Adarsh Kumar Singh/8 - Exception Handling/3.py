try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: ")) 
    try:
        result = numerator / denominator
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
