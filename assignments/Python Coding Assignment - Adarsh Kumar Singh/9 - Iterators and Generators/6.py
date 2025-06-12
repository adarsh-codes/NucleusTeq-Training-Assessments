def cartesian(list1,list2):
    for num in list1:
        for n in list2:
            yield (num,n)

list1 = [1,2]
list2 = [3,4]

for item in cartesian(list1,list2):
    print(item)
