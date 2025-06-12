with open('file2.txt','r+') as file:
       lines = file.readlines()
       non_empty_lines = [line for line in lines if line.strip() != ""]

with open('file2.txt', 'r+') as file:
    file.writelines(non_empty_lines)
    file.seek(0)
    print(file.read())

