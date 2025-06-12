
def count_words(file_content):
    words = file_content.split()
    print("Word count:", len(words))
          
with open('file.txt','r+') as file:
     file_scan = file.read()
     count_words(file_scan)


