# in Python 3 we have a 'context manager'
from contextlib import contextmanager # this is part of Python
import sys

@contextmanager # this applies the context manager functionality to our function
def std_outRedirect(new_stdout):
    '''Here we redirect output to a different stream'''
    save_stdout = sys.stdout
    sys.stdout  = new_stdout
    yield # our function will yield the next available object to be written
    sys.stdout = save_stdout # set things back how they were


if __name__ == '__main__':
    with open('temp_log.txt', 'a') as fobj:
        with std_outRedirect(fobj):
            print('This will be redirected to the log file')
    print('Back to the main console')