import re
hashtag = "lets #nope go to the #beach"
print(re.findall(r'#\w+',hashtag))