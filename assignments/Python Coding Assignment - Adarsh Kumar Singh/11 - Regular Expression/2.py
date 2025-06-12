import re
string = "123-456-7890"
phone = r'\d{3}-\d{3}-\d{4}'
print(bool(re.match(phone,string)))