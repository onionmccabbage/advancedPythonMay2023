from class_b import Figure

# ask the user for values
s = input('How many sides ? ') # remember - ALL inputs are STRING!!!
c = input('What colour ? ')
d = input('what size ? ')

# use these values to build an instance of a class
# be careful - if you need an int, first make a float then an int
my_shape = Figure(int(float(s)), c, float(d)) # we need to cast strings to numbers

print(my_shape)