# Python Classes encapsulate functionality
# Unlike other languages there is NO data-type-safety and NO public/private

class Shape():
    '''It is common practice to document your classes with a docstring
       Every method of a class must take 'self' as an argument'''
    def __init__(self, num_sides):
        '''the __init__ method is similar to a constructor.
           Runs every time we instantiate the class'''
        self.sides = num_sides # here we assign a property to this class

if __name__ == '__main__':
    '''here we can exercise the code. E.G. make instances of the class'''
    square = Shape('four') # the __init__ method will be called
    triangle = Shape(3)
    print(square.sides, triangle.sides)