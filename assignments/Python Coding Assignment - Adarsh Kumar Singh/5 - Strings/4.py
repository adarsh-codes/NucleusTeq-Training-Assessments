def count_in_string(string):
    count_words = 1
    count_char = 0
    count_lines = 0
    for char in string:
        if char == " ":
            count_words += 1
        elif char == ".":
            count_lines += 1
        else:
            count_char += 1
    return [count_char,count_lines,count_words]

string = input("Enter : ")
cnt1,cnt2,cnt3 = count_in_string(string)
print("No. of words :",cnt3)
print("No. of lines :",cnt2)
print("No. of characters :",cnt1)