
print("Simple calculator (+ , - , / , *)")
print("Give expression : ")
expression = input()

try:
 result = eval(expression)
 print("RESULT :",result)
 
except ZeroDivisionError:
 print("Can't divide by zero.")

except Exception:
 print("Unsupported Expression.") 
 
