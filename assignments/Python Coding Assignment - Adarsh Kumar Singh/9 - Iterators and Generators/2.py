class Fibo:
    def __init__(self,number):
        self.number = number
        self.count = 0
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.number:
            raise StopIteration
        
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val
        
fib = Fibo(5)

for num in fib:
    print(num)