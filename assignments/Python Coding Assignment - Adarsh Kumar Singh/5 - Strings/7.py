def caesar_cipher_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher_encrypt(text, shift)
print("Encrypted text:", encrypted)
