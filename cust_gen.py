# we have genersators built in to Python
# they are useful whenever we have loads of values but we need to avoid storing in memory

# Careful = [] would make a list (all values in memory)
my_numbers_g = (n for n in range(-99, 100)) # from -99 to 99
print(my_numbers_g) # we have a generator object (no values stored in memory)

# we can apply logic as we generate values
odd_g = (n for n in range(-99, 100) if n%2==1)

print( odd_g.__next__() ) # -99
print( odd_g.__next__() ) # -97
print( odd_g.__next__() ) # -95
print( odd_g.__next__() ) # -93

# we can write our own custom generator
def my_gen(first=0, last=10*100, step=1):
    '''generate values and yield the results'''
    number = first
    while number < last:
        yield number*number # the yield statement makes this a generator
        number += step

if __name__ == '__main__':
    g = my_gen() # g is an instance of our generator
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    # we can iterate over our generator
    for i in g:
        print(i, end=', ')
    # after use, the generator is exhausted - we would need a new instance to use it again
