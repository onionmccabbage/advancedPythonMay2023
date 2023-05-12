# All threads for a particular execution share the same resources
# There is ONE copy of Python, ONE set of data (memory, DB, file I/O etc)
# Each thread has it's own heap of memory once running
# We need to lock shared resources to make them 'thread safe'
import threading
import time
import random
# e.g. here is a value in the global namespace
counter = 0
# we need a global lock for hte threads to share
lock = threading.Lock()

def workerA():
    '''This worker will access the counter to increment it up to 10'''
    global counter # we now have access to the global variable called counter
    lock.acquire() # worker A now has exclusive access to the lock
    try:
        while counter <10:
            counter+= 1
            print(f'Worker A is incrementing counter to {counter}')
            time.sleep(random.randint(0,1)) # a random sleep of 0 or 1 seconds
    except Exception as err:
        print(f'Something went wrong {err}')
    finally:
        lock.release()

def workerB():
    '''This worker will access the counter to decrement it to -10'''
    global counter # we now have access to the global variable called counter
    lock.acquire() # worker B now has exclusive access to the lock (after A has finished with it)
    try:
        while counter >-10:
            counter-= 1
            print(f'Worker B is decrementing counter to {counter}')
            time.sleep(random.randint(0,1)) # a random sleep of 0 or 1 seconds
    except Exception as err:
        print(f'Something went wrong {err}')
    finally:
        lock.release()

if __name__ == '__main__':
    # sequentially, whichever gets to counter first will keep it until done
    # workerB()
    # workerA()
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    # since we have two threads they will BOTH tyr to acess counter together
    t2.start()
    t1.start() # whichever thread starts first will have first dibs on the lock
    t1.join()
    t2.join()
