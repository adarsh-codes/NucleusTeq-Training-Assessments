def compose(*functions):
    def composed_function(arg):
        result = arg
        for f in reversed(functions):
            result = f(result)
        return result
    return composed_function
def double(x):
    return x * 2

def square(x):
    return x ** 2

def increment(x):
    return x + 1

composed = compose(increment, square, double)

print(composed(2))
