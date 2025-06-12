import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {execution_time: .6f} seconds")
    return wrapper

@measure_time
def function():
    print("Function completed.",2*3*5*6)

function()