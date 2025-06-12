with open('file.txt','r+') as file:
    for line_number, line in enumerate(file,start=1):
        print(f"{line_number}:",f"{line}")