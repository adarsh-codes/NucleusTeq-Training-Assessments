import logging

def generate_even_upto(number):
    for i in range(0,number+1):
        if(i%2==0):
         yield i

try:
   number = int(input("Enter a number : "))
   for i in generate_even_upto(number):
       print(i)
except ValueError:
   logging.warning("Enter only integers.")
