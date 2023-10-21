# Nececaries to make decorators work, pass functions as params.

def hello(func):
    func()

def greet():
    print('still here')


a = hello(greet)

print(a)

# Higher order function aka HOC

# The HOC
def first(func):
    func()

# The HOC that returns another function
def second():
    def func():
        return 5
    return func

# Map, reduce and filter are also HOCs

# .map()
# .reduce()
# .filter()

# Decorators - modify the call without modifying the original function.
def my_decorator(func):
    # Now unpacks args and keyword args independent of how many params is passed.
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func

@my_decorator
def hello(input, smile=':)'):
    print(input, smile)

#@my_decorator
#def bye():
    #print('cya')

#hello()

#bye()

#a = my_decorator(hello)
#a()

#my_decorator(hello)()


a = my_decorator(hello)
a('hi')

