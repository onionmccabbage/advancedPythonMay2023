# closure is a design pattern across many languages inc Python
# it lets us be more choosy as to when we actually invoke a function

def minions(saying):
    def inner():
        return f'Minions say {saying}'
    # remeber, functions are objects like everything else
    return inner # NB no brackets (so the function is not invoked)

if __name__ == '__main__':
    a = minions('heheeheeheee')
    b = minions('hahaahaaahaa')

    # what have we got so far?
    print(a,b)

    # # we can then shoose to call the resulting function
    print( a() ) # the brackets invoke the function (a closure)
    print( b() )
