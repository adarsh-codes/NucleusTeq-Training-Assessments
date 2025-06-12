import re
text = "Here is a fake IP: 12345678.12345678.12345678.12345678 and some other text."
print(re.findall(r'\d{8}\.\d{8}\.\d{8}\.\d{8}',text))