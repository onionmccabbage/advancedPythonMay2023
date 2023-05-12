# we can declare a class and make it iterable

class Evens:
    '''This class lets us iterate over even numbers'''
    def __init__(self, limit):
        self.limit = limit
        self.val = 0
    def __iter__(self):
        '''To make a class iterable simpy override the __iter__ method'''
        return self # simple as that
    def __next__(self):
        '''by overriding the __next__ operator we can supply iterable values'''
        if self.val > self.limit:
            raise StopIteration # all done, nothing else to show
        else:
            rval = self.val
            self.val +=2
            return rval
        
if __name__ == '__main__':
    e = Evens(4) # we can make an iterable instance of our class
    print(e.__next__()) # 0
    # or we can just iterate the class
    for i in Evens(12):
        print(i)