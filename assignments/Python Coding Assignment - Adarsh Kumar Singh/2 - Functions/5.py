
string = input("Give a string : ")

vowels = ["a","e","i","o","u"]
count = 0
for char in string:
   if(char in vowels):
      count += 1

print("Number of vowels in string :",count)