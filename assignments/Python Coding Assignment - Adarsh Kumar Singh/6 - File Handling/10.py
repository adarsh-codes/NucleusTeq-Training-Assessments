def replace_words_in_file(filename, old_word, new_word):
    with open(filename, 'r') as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open(filename, 'w') as file:
        file.write(content)
    print("Replacement done!")

replace_words_in_file('file2.txt', 'line', 'newline')
