from threading import Thread
import time
import random
from typing import Any

# here is a callable class (it does not inherit from Thread)
class MyClass: # implicitly iherit from object
    '''This class does not inherit anything from Thread'''
    def __call__(self, n):
        for i in range(1, 50): # emulate a long running outcome
            print(f'{n} is sleeping')
            time.sleep(random.random()*0.1)

if __name__ == '__main__':
    start = time.time()
    c1 = MyClass() # we can target a class or function as many times as we like
    my_threads_l = [] # a list to contain our thread instances
    # no matter how many threads, it will always be faster than sequential operation
    for _ in range(0, 256):
        my_threads_l.append( Thread(target=c1, args=(str(_),)) ) # a one-member tuple 
    for item in my_threads_l:
        item.start()
    for item in my_threads_l:
        item.join()
    end = time.time()
    print(f'Total execution time was {end-start}')