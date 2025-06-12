string = input("Enter a string : ")

with open('file2.txt','a+') as file:
    file.seek(0)
    print("Original content :",file.read())
    file.write(string)
    file.seek(0)
    print("Updated content :",file.read())
    