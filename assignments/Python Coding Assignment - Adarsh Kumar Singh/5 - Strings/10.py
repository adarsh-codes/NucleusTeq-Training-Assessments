def compress_string(string):
    result = ""
    curr_char = string[0]
    curr_count = 1
    for char in string[1:]:
        if char == curr_char:
            curr_count += 1
        else:
            result += curr_char+f"{curr_count}"
            curr_char = char
            curr_count = 1
    result += curr_char+f"{curr_count}"
    return result

string = input("Enter a string :")
print("Original String :",string)
print("Compressed String :",compress_string(string))