import time
from threading import Thread, Event

# global objects
event = Event() # this allows communication from the main thread to child threads

class MyClass:
    def __call__(self, n):
        global event
        print(f'{n} is waiting for an event notification')
        event.wait() # the thread will pause until it receives notification
        print(f'{n} proceeding after event notification')

def main():
    global event
    c1 = MyClass()
    thread_l = []
    for _ in range(8):
        thread_l.append( Thread(target=c1, args=(str(_),)) )
    for thread in thread_l:    
        thread.start()
    time.sleep(3) # the main thread will sleep for 3 seconds
    event.set() # this is where the event is triggered
    for thread in thread_l:
        thread.join() # careful - join can lock the event noticifaction!

if __name__ == '__main__':
    main()