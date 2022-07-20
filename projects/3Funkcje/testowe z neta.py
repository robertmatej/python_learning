from datetime import datetime


def log_before_and_after(func):
    def wrapper():
        print(f"start{datetime.now()}")
        result = datetime.now()
        print(f"stop{datetime.now()}")
        return result
    return wrapper

def run_only_between(_from=7, _to=22):
    def real_decorator(func):
        def wrapper():
            if _from <= datetime.now().hour < _to:
                func()
            else:
                pass
        return wrapper
    return real_decorator

@log_before_and_after
@run_only_between(7, 22)
def say_something():
    print("Hello!!")

say_something()