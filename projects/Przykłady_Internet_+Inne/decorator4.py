import time

def decor (function):

    def wrapper(*args, **kwargs):
        start = time.time()
        x = function(*args, **kwargs)
        stop = time.time()
        print(f" Function {function.__name__} take to work { round(stop - start,2)} s")
        return x

    return wrapper

@decor
def timemeter():
    print("Hello my friend ;)")
    time.sleep(1)

@decor
def power(a, b):
    return a ** b

timemeter()
print (f"Result is: {power(29, 3)}")