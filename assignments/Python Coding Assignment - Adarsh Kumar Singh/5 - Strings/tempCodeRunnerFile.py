def is_strong_password(password):
    special_chars = "!@#$%^&*(),.?\":{}|<>"

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if not has_upper:
        return False, "Password must contain at least one uppercase letter."
    if not has_lower:
        return False, "Password must contain at least one lowercase letter."
    if not has_digit:
        return False, "Password must contain at least one digit."
    if not has_special:
        return False, "Password must contain at least one special character."

    return True, f"Strong password: {password}"

password = input("Enter your password: ")
valid, message = is_strong_password(password)
print(message)
