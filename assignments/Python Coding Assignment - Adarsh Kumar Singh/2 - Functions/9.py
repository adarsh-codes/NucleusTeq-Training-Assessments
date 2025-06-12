
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item,list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested_list = [1,2,[4,5,76,23],43,4]
result = flatten_list(nested_list)
print("Flattened List :",result)
