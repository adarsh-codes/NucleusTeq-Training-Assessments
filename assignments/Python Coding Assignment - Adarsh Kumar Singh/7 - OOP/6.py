class CustomList:
    def __init__(self, data=None):
        self.items = data if data is not None else []

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __len__(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

    def append(self, value):
        self.items.append(value)

    def __iter__(self):
        return iter(self.items)

clist = CustomList([10, 20, 30])
print("Initial:", clist)

clist.append(40)
print("After append:", clist)

print("Element at index 1:", clist[1])

clist[2] = 99
print("After update:", clist)

print("Length:", len(clist))

for val in clist:
    print("Iterated value:", val)
