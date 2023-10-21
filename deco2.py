# Decorators part 2

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} ms')
        return result
    return wrapper

@performance
def long_time():
    # Just does a large calculation used to messure time taken
    for i in range(1000000):
        i * 5

long_time()