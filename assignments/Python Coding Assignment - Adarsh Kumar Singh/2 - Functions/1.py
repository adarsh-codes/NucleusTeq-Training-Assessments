
def factorial(x):
  value = 1
  for i in range(1,x+1):
    value = value * i
  return value

x = int(input("Give a number :"))
print("Factorial of",x,"is",factorial(x))


