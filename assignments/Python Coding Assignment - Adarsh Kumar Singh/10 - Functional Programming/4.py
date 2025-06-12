def apply_function(function,list_1):
    result = []
    for item in list_1:
        result.append(function(item))
    return result

def square(num):
    return num**2

custom_list = [1,2,3]
print(apply_function(square,custom_list))
