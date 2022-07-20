"""
dekorator wypisujący wywołanie danje finkcji: (nazwa i argmenty) oraz czas jej wykonania

"""
from datetime import datetime

def dekor_czas (func):
    def wrapper ():
        if func():
            start = datetime.now()
            print (f'Wykonano: {start}, nazwa funkcji to: {func} {func()}')
        #return start
    return wrapper

@dekor_czas
def foo(arg ="loolz"):
    return f' z arg "{arg}"'

foo()

