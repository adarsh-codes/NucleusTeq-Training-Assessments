def line_by_line(file):
    with open(file,'r') as f:
        for line in f:
            yield line

for line in line_by_line('file.txt'):
    print(line)