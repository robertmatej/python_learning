def decor (function):
    def wrapper():
        print(f"decoring function{function.__name__}")
        return function()
    return wrapper

@decor
def function1 ():
    print("I'm function 1")

@decor
def function2 ():
    print("I'm function 2")

function1()
function2()

#test