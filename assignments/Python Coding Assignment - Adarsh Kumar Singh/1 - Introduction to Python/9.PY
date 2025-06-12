print("Give n : ")
n = int(input())

first = 0
second = 1
i = 0

while i < n:
 print(first,end=" ")
 first,second = second,first+second
 i += 1