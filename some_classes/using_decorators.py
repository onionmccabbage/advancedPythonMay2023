# using decorators to implement class methods (and class properties)
class Duck():
    # we can have properties that belong to the class
    count = 0
    def __init__(self, n):
        '''persist the value of n'''
        self.__n = n
        Duck.count += 1 # count belongs to the class
    @classmethod
    def howMany(cls): # NB class methods do not take 'self'
        print(f'Duck class has {cls.count} instances')

if __name__ == '__main__':
    d1 = Duck('Howard')
    d2 = Duck('Mallard')
    d3 = Duck('Eider')
    d4 = Duck('Donald')
    print(Duck.count)
    Duck.howMany() # call our class method