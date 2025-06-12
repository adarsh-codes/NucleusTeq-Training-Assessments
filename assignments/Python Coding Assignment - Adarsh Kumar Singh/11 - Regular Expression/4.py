import re
string = "This is Adarsh. I work at Nucleusteq."
print(re.findall(r'[A-Z][a-zA-Z0-9]*',string))