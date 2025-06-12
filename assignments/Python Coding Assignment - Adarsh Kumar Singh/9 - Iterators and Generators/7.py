def filter_palindrome(list1):
    for word in list1:
        if word == word[::-1]:
            continue
        else:
            yield word

list1 = ['words','tenet','abcd','aeiea']

for word in filter_palindrome(list1):
    print(word)