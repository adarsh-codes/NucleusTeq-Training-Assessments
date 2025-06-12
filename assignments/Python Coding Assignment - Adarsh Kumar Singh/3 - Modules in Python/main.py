# using mypackage in main.py
from mypackage import math_ops, string_ops

print("Add:", math_ops.add(10, 5))
print("Subtract:", math_ops.subtract(10, 3))

print("Reverse:", string_ops.reverse_string("hello"))
print("Capitalized:", string_ops.capitalize_words("hello world"))