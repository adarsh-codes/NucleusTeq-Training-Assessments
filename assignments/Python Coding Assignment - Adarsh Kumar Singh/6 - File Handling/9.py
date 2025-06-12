def count_frequency(string):
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    print("Frequencies :",freq)

with open('file.txt','r') as file:
    content = file.read()
    count_frequency(content)