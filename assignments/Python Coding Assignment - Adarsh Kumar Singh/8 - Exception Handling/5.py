try:
    file = open("file.txt", "r")
    content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: An I/O error occurred.")
finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so nothing to close.")
