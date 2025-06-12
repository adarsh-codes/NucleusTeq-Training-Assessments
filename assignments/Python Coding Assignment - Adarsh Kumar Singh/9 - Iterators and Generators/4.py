class StringIterator:
    def __init__(self,string):
        self.string = string
        self.count = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.string):
            raise StopIteration
        
        else:
            index = self.count
            self.count += 1
            return self.string[index]

s = StringIterator("ABCDEFGHI")

for ch in s:
    print(ch)