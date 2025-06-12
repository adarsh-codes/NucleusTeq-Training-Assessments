#Build a regex to validate complex passwords (at least 1 digit, 1 symbol, 8+ chars).

import re
pattern = r'^(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$'
print(bool(re.fullmatch(pattern,'n@qwerQ123214')))