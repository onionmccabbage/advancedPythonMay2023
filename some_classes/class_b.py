# we can import from other modules
from class_a import Shape

# NB EVERYTHING in Python inherits from 'object'

# we can also extend ANY class
# class Abstract(object): # here we explicitly inherit from the Python 'object' class
class Abstract: # the brackets are optional. Here we IMPLICITLY inherit from 'object'
    '''This is the most generic class possible - it has no properties or methods'''

class Basic(Abstract): # we can only inherit from a single parent class
    '''This class inherits everything from Abstract'''
    def __init__(self, x, y):
        self.x = x # we could use name mangling, but not obliged to do so
        self.y = y

class Concrete(Basic):
    def __init__(self, x, y, z):
        # Basic.__init__(x, y) # here we call the __init__ method of hte parent class
        super().__init__(x, y) # 
        self.z = z

# here we will declare a class that inheriots from 'Shape' and adds a 'size' property
class Figure(Shape):
    def __init__(self, num_sides, colour, size):
        super().__init__(num_sides, colour) # let the parent deal with these proeprties
        ''' validate the 'size' to be a positive floating point number'''
        self.size = size  #remember - this will call the setter method
    @property
    def size(self):
        '''this is the getter, so just return the value'''
        return self.__size
    @size.setter
    def size(self, size):
        if isinstance(size, float) and size > 0:
            self.__size = size # use name mangling
        else:
            self.__size = 1.0
    def __str__(self): # override the __str__ of the parent
        return f'This {self.colour} shape is size {self.size} with {self.sides} sides'

if __name__ == '__main__':
    pentagon = Figure(15, 'green', 3.25)
    pentagon.sides = 5
    # we can mutate any properties - they will be validated
    pentagon.size = 99.9
    pentagon.colour= True # this will fail and default to grey
    print(pentagon)
