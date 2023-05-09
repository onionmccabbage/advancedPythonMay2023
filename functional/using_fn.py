# instead of using classes many coding solutions only need functions
# a 'pure' function is entirely predictable for given inputs
# an 'impure' function cannot be predicted (e.g. random)
from functools import reduce

def squareIt(x):
    '''return the square of a number'''
    return x**2 # or x*x

def addThem(x, y):
    '''return the sum of two numbers'''
    return x+y

def isOdd(n):
    '''return True of False depending on if hte number is odd or even'''
    return n%2 !=0 # modulo: return what is left over after integer division

if __name__ == '__main__':
    print(squareIt(4)) # 16
    print(addThem(3, 7)) # 10
    print(isOdd(-9)) # True
    # suppose we need a tuple of square numbers in a range
    sq_t = tuple( map(squareIt, range(1, 12)) ) # apply the function to every member in the range
    print(sq_t)
    # Now what if we need a huuuuuuuge number of values...
    # Better to make a generator, so the resulting values do not need to persist in memory
    sq_g = map(squareIt, range(1, 10**2)) # we now have a generator (a map object)
    print( sq_g ) # NB the resulting values do NOT persist in memory
    # we can yield the next available value like this...
    print( sq_g.__next__() ) # 1
    print( sq_g.__next__() ) # 4
    print( sq_g.__next__() ) # 9
    print( sq_g.__next__() ) # 16
    print( sq_g.__next__() ) # 25
    # once we have a map object, we can choose to iterate over it
    for item in sq_g:
        print(item, end=', ')
    # when all the values have been yielded, the map/generator is exhausted and cannot be used again

    # There is also a 'filter' capability in Python
    odd_l = list( filter( isOdd, range(1, 27) ) )
    print(odd_l)
    # or we can create a 'filter' generator object like this 
    odd_g = filter( isOdd, range(-10**10, 10**10) )
    print( odd_g.__next__() )
    print( odd_g.__next__() )
    print( odd_g.__next__() )
    print( odd_g.__next__() )
    # we might choose to iterate....

    # There is als oa 'reduce' method
    r = reduce( addThem, odd_g)
    print(r) # all the values iteratively added together
