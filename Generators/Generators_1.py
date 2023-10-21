
# interable
# iterate
# generators are interable but not all interables are generators

list # not a generator but an interable
range # a generator and interable

# using yield we can pass each element of a sequence in a range without creating one large orbject
# as 'item' is alwasys only 1 element
def generator_function(num):
    for i in range(num):
        yield i*2

#for item in generator_function(1000):
    #print(item)


# Since yeild pauses the function we can now step for each element and print(next(g)) returns '4'
# since we step 2 times first as 0*2 = 0, 1*2 = 2 and lastly 2*2 = 4.
g = generator_function(100)
next(g)
next(g)
print(next(g))

# as making a list stores in memory moving to using range instead to create at time is better.
"""
    def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result
    my_list = make_list(100)
    print(my_list)
    """