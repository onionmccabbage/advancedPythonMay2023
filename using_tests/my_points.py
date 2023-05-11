class Point: # implicitly inherit from object
    '''define a point in 2-d space represented by x and y as floating point values
       Also define moveBy to allow changes to x and y (i.e. move the point)
    '''
    def __init__(self, x, y):
        '''call setter methods for x and for y'''
        self.x = x # call the property setter for x
        self.y = y
    @property
    def x(self):
        return self.__x # return the 'mangled' property value
    @x.setter
    def x(self, x):
        if type(x)==float or type(x)==int:
            self.__x = x # set a mangled property for x (only visible within the class)
        else:
            raise TypeError
    @property
    def y(self):
        return self.__y # return the 'mangled' property value
    @y.setter
    def y(self, y):
        if type(y)==float or type(y)==int:
            self.__y = y # set a mangled property for x (only visible within the class)
        else:
            raise TypeError
    def moveBy(self, dx, dy):
        '''change the x and y values by dx and dy'''
        self.x += dx # self.x will invoke the SETTER method for self.__x
        self.y += dy
    def display(self):
        return (self.x, self.y)

if __name__ == '__main__':
    '''exercise the code'''
    p1 = Point(5, 7)
    p1.moveBy(2, -3)
    print(p1.x, p1.y) # 7 4
