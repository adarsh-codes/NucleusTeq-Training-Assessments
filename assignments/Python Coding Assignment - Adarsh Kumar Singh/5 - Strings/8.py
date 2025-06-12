def remove_html_tags(text):
    result = ""
    in_tag = False
    for char in text:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            result += char
    return result

html_string = "<h1>Hello, <b>World!</b></h1>"
clean_text = remove_html_tags(html_string)
print(clean_text)
