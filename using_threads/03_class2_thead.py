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
    t1 = Thread(target=c1, args=('1',)) # a one-member tuple
    t2 = Thread(target=c1, args=('2',)) # a one-member tuple
    t3 = Thread(target=c1, args=('3',)) # a one-member tuple
    t4 = Thread(target=c1, args=('4',)) # a one-member tuple
    t5 = Thread(target=c1, args=('5',)) # a one-member tuple
    t6 = Thread(target=c1, args=('6',)) # a one-member tuple
    t7 = Thread(target=c1, args=('7',)) # a one-member tuple
    t8 = Thread(target=c1, args=('8',)) # a one-member tuple
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    end = time.time()
    print(f'Total execution time was {end-start}')