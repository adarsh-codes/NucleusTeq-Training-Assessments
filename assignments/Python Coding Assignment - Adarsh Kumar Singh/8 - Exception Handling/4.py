class InvalidAgeError(Exception):
    def __init__(self, message="Age must be a positive integer between 0 and 120"):
        self.message = message
        super().__init__(self.message)

try:
    user_age = int(input("Enter your age: "))
    if(user_age > 0):
     print("Age :",user_age)
    else:
     raise InvalidAgeError("Invalid age, please provide a valid integer value. Age must be positive")
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Error: Please enter a valid number.")
