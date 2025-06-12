def format_currency(number):
    return "{:,}".format(number)

num_input = input("Enter a number: ")

try:
    number = int(num_input)
    formatted = format_currency(number)
    print("Formatted as currency:", formatted)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
