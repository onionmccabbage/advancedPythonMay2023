# CAREFUL - when you import, all immediate code will run
from class_b import Figure

# ask the user for values
s = input('How many sides ? ') # remember - ALL inputs are STRING!!!
c = input('What colour ? ')
d = input('what size ? ')

# use these values to build an instance of a class
# be careful - if you need an int, first make a float then an int
my_shape = Figure(int(float(s)), c, float(d)) # we need to cast strings to numbers

# it is a good idea to ALWAYS use the following line
# prevents any code executing on import
if __name__ == '__main__':
    # what is the name iof the module we are executing?
    print(__name__) # should be '__main__'
    print(my_shape)