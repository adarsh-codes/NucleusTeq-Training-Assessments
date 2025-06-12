class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True 

with FileManager("file.txt", "r") as f:
    content = f.read()
    print(content)
