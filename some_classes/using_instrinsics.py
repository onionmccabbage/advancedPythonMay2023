# There are many things built in to Python
# many of them ara available as 'intrinsic' properties

class TopLevel():
    '''Here is a docstring'''
    def __init__(self):
        pass # do nothing!!!

class Derived(TopLevel):
    '''This class is derived from TopLevel class'''
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    # we can explore some of the intrinsic properties provided by Python
    print( f'Class name is {Derived.__name__}' ) # careful - call on the class
    print( f'class docstring is {Derived.__doc__}')