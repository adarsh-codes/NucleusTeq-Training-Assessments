def remove_duplicates(list1):
    result = []
    for item in list1:
        if item not in result:
            result.append(item)
    return result

list1 = [1,2,3,3,4,4,4,5,6,6,6,6,6]
print("Original List :",list1)
print("Removed Duplicates :",remove_duplicates(list1))