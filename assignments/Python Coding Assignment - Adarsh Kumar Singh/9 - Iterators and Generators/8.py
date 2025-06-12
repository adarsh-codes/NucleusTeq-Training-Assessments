def infinite_fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a,b = b,a+b

fib = infinite_fibonacci()
for _ in range(10):
    print(next(fib),end=" ")