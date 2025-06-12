import re
string = "Hello  . This    is Adarsh."
result = re.sub(r'\s+','-',string)
print(result)