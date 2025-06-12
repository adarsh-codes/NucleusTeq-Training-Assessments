
def reverse_string(s):
    value = ""
    for i in range(len(s)-1,-1,-1):
       value += s[i]
    return value

s = input("Give a string : ")
result = reverse_string(s)
print(result)