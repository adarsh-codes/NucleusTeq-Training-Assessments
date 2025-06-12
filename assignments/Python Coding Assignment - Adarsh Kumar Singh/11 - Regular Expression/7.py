# dd-mm-yyyy
import re
string = "Who was born on 02-09-2000? And on 03-05-1999"
print(re.findall(r'\b\d{2}-\d{2}-\d{4}\b',string))
