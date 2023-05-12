from collections.abc import Callable, Iterable, Mapping
import threading
import time
import random
from typing import Any

# a global variable
ticketsAvailable = 100

class TicketSeller(threading.Thread):
    ticketsSold = 0 # this represents how manmy tickets sold by a ticket seller
    def __init__(self, lock):
        super().__init__(self) # or Thread.__init(self)
        self.__lock = lock
        print(f'Ticket seller started selling tickeets')
    def run(self):
        global ticketsAvailable
        running = True 
        while running:
            self.randomDelay()
            self.__lock.acquire() # grab the lock
            if(ticketsAvailable <=0):
                running = False
            else:
                self.ticketsSold += 1
                ticketsAvailable -= 1
                print(f'Sold a ticket, {ticketsAvailable} remaining')
            self.__lock.release()
        print(f'Sold {self.ticketsSold}')
    def randomDelay(self):
        time.sleep(random.randint(0, 4)/4) # 0, 0.25, 0.5 or 0.75 seconds

def main():
    '''here we create several ticket sellers all trying to sell tickets'''
    lock = threading.Lock()
    sellers_l = []
    for i in range(0 ,4):
        seller = TicketSeller(lock)
        sellers_l.append(seller)
        seller.start()
    for seller in sellers_l:
        seller.join()

if __name__ == '__main__':
    main()