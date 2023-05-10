import sys
# print (sys.stdout)

class Redirect():
    '''provide a way to redirect the standard output'''
    def __init__(self, new_stdout):
        '''receive a new stdout'''
        self.new_stdout = new_stdout # we ought to validate this...
    # next we override __enter__ and also __exit__
    # (they run every time the instance starts and ends)
    def __enter__(self):
        '''implement the redirect'''
        self.save_stdout = sys.stdout # capture the current stdout
        sys.stdout = self.new_stdout  # set our new stdout
    def __exit__(self, exc_type, exc_value, exc_traceback): # these are required!!
        '''return to the original stdout'''
        sys.stdout = self.save_stdout # restore whatever stdout was when we started

if __name__ == '__main__':
    # we really should use try-except here
    with open('temp_log.txt', 'w') as fobj: # the 'with' operator will close the file access object when done
        with Redirect(fobj):
            print('This will be written to our log file')
    print('We are back with the default stdout (the console)')