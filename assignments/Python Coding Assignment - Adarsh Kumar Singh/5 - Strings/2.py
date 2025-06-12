def find_substrings(text):
        substrings = []
        length = len(text)
        for i in range(length):
            for j in range(i + 1, length + 1):
                substrings.append(text[i:j])

        return substrings

user_input = input("Enter a string: ")
result = find_substrings(user_input)
print("All substrings:")
for s in result:
    print(s)
