with open('file2.txt','r+') as file:
    file_content = file.read()
    with open('file.txt','a+') as fileobj:
        fileobj.write(file_content)
        fileobj.seek(0)
        print("Read content :",fileobj.read())