import re
string = "hello. please contact at adarsh@gmail.com or adarsh@company.com"
result = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+\.com',string)
print(result)