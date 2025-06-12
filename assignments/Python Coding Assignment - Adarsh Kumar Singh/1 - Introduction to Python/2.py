print("Give three numbers :")
x = int(input())
y = int(input())
z = int(input())

if(x >= y and x >= z):
    print("Greatest is :",x)

elif(y >= x and y >= z):
    print("Greatest is :",y)

else:
    print("Greatest is :",z)