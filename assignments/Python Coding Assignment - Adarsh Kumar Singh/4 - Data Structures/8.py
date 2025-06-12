def intersection(list1, list2):
    return list(set(list1) & set(list2))

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
print("Intersection:", intersection(a, b))
