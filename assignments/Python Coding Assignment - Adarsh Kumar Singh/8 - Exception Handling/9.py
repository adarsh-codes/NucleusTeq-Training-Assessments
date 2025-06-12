def decorator(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            print(str(e))
    return wrapper

@decorator
def divide(a, b):
    print(a / b)

divide(10, 0)