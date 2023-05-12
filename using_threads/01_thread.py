from threading import Thread
import random
import time
# All python code runs on the 'main' thread

def myFn(n):
    '''This is a normal function. Like all functions it can be invoked on a new thread
       This allows concurrent code to be executed alongside each other. 
       This can make our code faster'''
    for i in range(1, 50): # this will take about 2.5 seconds (just over)
        print(f'{n} is sleeping')
        time.sleep( random.random()*0.1 ) # here we might be doing a long-running outcome

if __name__ == '__main__':
    '''we can target any function to be run as a separate Thread'''
    start = time.time()
    # not using threads (i.e. sequential code)
    # myFn('A')
    # myFn('B') # takes about 5-6 seconds
    t1 = Thread(target=myFn, args=('1',) ) # arguments must be a tuple
    t2 = Thread(target=myFn, args=('2',) ) # the comma ensures we have a one-member tuple
    t3 = Thread(target=myFn, args=('3',) ) 
    t4 = Thread(target=myFn, args=('4',) )
    # next we must start these new threads
    t1.start() # at this point our function begins to be executed on a separate thread
    t2.start() 
    t3.start() 
    t4.start() 
    # we need to let our threads join back to the main thread
    t1.join()
    t2.join() # good practice: join threads at the earliest opportunity
    t3.join()
    t4.join()
    end = time.time()
    # we can run additional code on the main thread because we used 'join'
    print(f'Total execution time is {end-start}') # takes about 3 seconds
