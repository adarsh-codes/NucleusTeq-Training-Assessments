def replace_vowel(string):
    result = ""
    for char in string:
        if char in ['a','e','i','o','u','A','E','I','O','U']:
            result += "*"
        else:
            result += char
    return result

string = input("Enter a string : ")
print("Vowels replaced :",replace_vowel(string))
