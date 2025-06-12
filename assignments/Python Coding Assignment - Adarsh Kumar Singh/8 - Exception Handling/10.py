class InvalidAgeError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class UnauthorizedAccessError(Exception):
    pass

def register_user(age):
    if age < 18:
        raise InvalidAgeError("User must be at least 18 years old.")
    print("User registered successfully.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance to withdraw.")
    print(f"Withdrew Rs.{amount} successfully.")

def access_secure_data(role):
    if role != "admin":
        raise UnauthorizedAccessError("Access denied: Admins only.")
    print("Access granted to secure data.")

try:
    register_user(16)
except InvalidAgeError as e:
    print("Age Error:", e)

try:
    withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print("Balance Error:", e)

try:
    access_secure_data("guest")
except UnauthorizedAccessError as e:
    print("Access Error:", e)

