import logging

try:
    divide = 12/0
    print("Result :",divide)
except Exception as Argument:
    with open('logfile.txt','a') as file:
        file.write(str(Argument))