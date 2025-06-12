import re
pattern = r'\w+|[^\w\s]'
print(re.findall(pattern,"Hello, world! How's everything? (Good, I hope.)"))