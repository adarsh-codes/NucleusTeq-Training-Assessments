import random

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for complexity."
    
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    characters = uppercase_letters + lowercase_letters + digits + special_chars

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter password length: "))
    print("Generated password:", generate_password(length))
except ValueError:
    print("Please enter a valid integer.")
