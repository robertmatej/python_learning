import time

def decor(func):
    def wrapper (*args, **kwargs):
        start = time.time()
        func(*args,**kwargs)
        stop = time.time()
        return f"time: {round(stop - start,2)} in {func.__name__} with arguments: {args, kwargs}"
    return wrapper

@decor
def simple_function(a, b):
    print("Simple function")
    time.sleep(0.5)

print(simple_function(2,3))
