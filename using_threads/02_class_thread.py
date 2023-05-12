from threading import Thread
import time
import random

# NB 'Thread' is a means by which we access a thread (it is not a thread itself)
# We inherit from the Thread class
class MyClass(Thread):
    '''This class can me invoked on a new thread
       Here we simulate long-running outcomes by sleeping'''
    def __init__(self, n):
        # super().__init__(self) 
        Thread.__init__(self) # call the initializer of the parent class (Thread)
        self.n = n
    # in order to be runnable we override the 'run' method of thread
    def run(self):
        '''When this (thread) class is invoked, this run method will be automatically called
           therefore this class will always be run on a separate thread'''
        for i in range(1, 50):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1)

if __name__ == '__main__':
    start = time.time()
    c1 = MyClass('1')
    c2 = MyClass('2')
    # start
    c1.start() # this will invoke the 'run' method
    c2.start()
    # join
    c1.join()
    c2.join()
    end = time.time()
    print(f'Total time was {end-start}')