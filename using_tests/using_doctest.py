import doctest # built in to Python

def cube(x):
    '''return the cube of a number
    >>> cube(3)
    27
    >>> cube(-1)
    -1
    '''
    return x*x*x

def squares(a,b):
    '''return all the squares between a and b
    >>> squares(1,6)
    [1, 4, 9, 16, 25, 36]
    >>> squares(1, 10) # doctest:+ELLIPSIS
    [1, 4, ..., 100]
    '''
    answer_l = []
    for i in range(a, b+1):
        answer_l.append(i*i)
    return answer_l

def squareIt(x):
    '''return the square of any value less than ten, raise exceptino for ten or more
    >>> squareIt(3)
    9
    >>> squareIt(30)
    Traceback (most recent call last):
    ...
    ValueError: Value must be less than ten
    '''
    if x>=10:
        raise ValueError('Value must be less than ten') # or Exception
    else:
        return x*x

if __name__ == '__main__':
    # print( cube(3) ) # 27
    # print(squares(1,6)) # [1, 4, 9, 16, 25, 36]
    # print(squareIt(30))
    # we can allow ellipsis like this...
    doctest.testmod( optionflags=doctest.NORMALIZE_WHITESPACE, verbose=True ) # this will invoke any tests within the documentation sting