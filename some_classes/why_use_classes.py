# Only use a class if nothing else will do
# logic
flag = True # boolean is handy
# numbers
age = 37 # an integer
intelligence = 189.64 # floating pouint number
print(type(age))
# text
greet = 'hello and welcome'
print(greet[0:6])
# collections
my_tup = (4, 7, 3, age, flag, 'more') # immutable collection of any types
my_list = [4, 7, 3, age, flag, 'more'] # mutable collection
my_set = {6, 4, 4, 8, 1, False} # unique members
my_dictionary = {'name':'Floella', 'hero':True} # not indexed by number
print(my_set)