# There are several ways to pass arguments into functions
def fnA(*args): # *args stands for all the positional arguments
    print(args) # all the positional arguments end up in a tuple

def fnB(**kwargs): # **kwargs stands for all the keyword arguments
    print(kwargs) # all the keyword arguments end up in a dictionary

def fnC(*args, **kwargs): # careful args must come before kwargs
    print(args, kwargs)

# NB it is only a convention to say 'args' and 'kwargs'

if __name__ == '__main__':
    fnA(0, 1, True, {}, [], (3,2,1), 'hello')
    fnB(w=False, x =(4,3,2), z=9, y=[])
    fnC( 'hello', [], (1,), c={}, other=fnA )