# Python Classes encapsulate functionality
# Unlike other languages there is NO data-type-safety and NO public/private

class Shape():
    '''It is common practice to document your classes with a docstring
       Every method of a class must take 'self' as an argument
       This class will capture the number of sides and the colour of a shape'''
    def __init__(self, num_sides, colour=''): # we can provide defaults
        '''the __init__ method is similar to a constructor.
           Runs every time we instantiate the class'''
        # self.checkSides(num_sides) # here we assign a property to this class
        self.sides = num_sides # here we assign a property to this class (calling the method)
        # self.checkColour(colour)
        # we can use 'name-mangling' to protect properties
        self.colour = colour # even though this looks like a property, it will call the setter method
    # we can declare methods to validate the parameters
    @property
    def sides(self): # NB the name of the function must match the name of the property
        return self.__sides
    @sides.setter
    def sides(self, num_sides):
        '''Validate the number of sides is a non-zero positive integer'''
        if type(num_sides)==int and num_sides > 0:
            ''' all good '''
            self.__sides = num_sides
        else:
            '''not valid...'''
            raise Exception('number of sides must be a positive integer')
    
    # we use 'decorators' to set and get properties
    @property
    def colour(self): # even though this is a method, it will appear as a property
        return self.__colour # by using double-underscore, we 'mangle' the name of this property
    @colour.setter # this is the setter method for the property
    def colour(self, colour):
        '''Check the colour is a non-empty string, or set a default'''
        if isinstance(colour, str) and colour !='':
            '''all good'''
            self.__colour = colour
        else: # set a default
            self.__colour = 'grey'
    def __str__(self): # here we override the built-in __str__ method with our own
        '''The __str__ method will be used by any print call'''
        return f'This shape has {self.sides} sides and is {self.colour}'
    def __repr__(self): # here we override the built-in __repr__ method
        '''the __repr__ method will be only be used in immediate mode (NOT by print)'''
        return f'This {self.colour} shape has {self.sides} sides'

if __name__ == '__main__':
    '''here we can exercise the code. E.G. make instances of the class'''
    # square = Shape('four', 'Blue') # 
    square = Shape(4, 'Blue') # the __init__ method will be called
    triangle = Shape(3, 'Yellow')
    hexagon = Shape(6) # use the default colour setting
    # we can mutate properties of our class
    # square.colour = 'orange' # this will call the @property setter method
    square.__colour = 'orange' # careful - we have created a new, arbitrary property called 'colour'
    print(square.__repr__(), square.__colour)
    print(hexagon)
