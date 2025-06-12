def read_lines(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line

def clean_lines(lines):
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            yield cleaned

def split_words(lines):
    for line in lines:
        for word in line.split():
            yield word

lines = read_lines('file.txt')
cleaned_lines = clean_lines(lines)
words = split_words(cleaned_lines)

for line in words:
    print(line)
