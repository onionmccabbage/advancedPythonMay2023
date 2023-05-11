import unittest
from my_points import Point

# NB we use 'test' in the class name
class testPoint(unittest.TestCase): # inherit from TestCase
    '''here are tests for the Point class'''
    # declare setup to run before every test
    def setUp(self):
        '''this method will be automatically called before each test is run'''
        self.point = Point(3, 5) # each test will begin with a new point

    # declare independent tests
    def testMoveBy1(self): # NB we MUST begin tests with the word 'test'
        '''Test the moveBy method'''
        self.point.moveBy(5, 2)
        self.assertEqual(self.point.x, 8) # we expect the point to be at 3+5 ie 8
        self.assertEqual(self.point.y, 7)
    def testMoveBy2(self): # NB we MUST begin tests with the word 'test'
        '''Test the moveBy method'''
        self.point.moveBy(-5, -2)
        self.assertEqual(self.point.x, -2) # we expect the point to be at 3-5 ie -2
        self.assertEqual(self.point.y, 3)

if __name__ == '__main__':
    unittest.main() # this will run all our tests