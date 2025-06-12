from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    print("Opening file...")
    f = open(path, mode)
    try:
        print("yield run")
        yield f
    finally:
        print("Closing file...")
        f.close()

with open_file('file.txt', 'a') as file:
    file.write("Hello from context manager")

