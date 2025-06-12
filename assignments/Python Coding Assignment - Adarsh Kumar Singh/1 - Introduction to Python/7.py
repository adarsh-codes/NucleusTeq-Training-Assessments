
print("Give the number :")
try:
 number = int(input())
 factors = 0
 for i in range(1,number+1):
    if(number % i == 0):
     factors += 1

 if(factors == 2):
   print(number,"is prime.")
 else:
   print(number,"is not prime.")
except ValueError:
 print("Please enter only an integer.")

