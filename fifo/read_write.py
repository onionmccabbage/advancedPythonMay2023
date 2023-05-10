# we can read and write text, byte etc with persistent files
# Python provides file access objects for this

# write text (defaults to text)
fout = open('snip.txt', 'at') # 'a' will append, 'w' will (over)write, 'x' for exclusive access
# NB print will automatically put a newline at the end of each output
print('here is some content', file=fout ) # re-direct the print oputput to a text file
# we have a file access object - not the file, but a means by which we access the file
# always a good idea to tidy up
fout.close()

# often we need more control over writing to file
def writeToFile(text): # we ought to validate the incoming to make sure it is text
    '''write long strings of text a chunk at a time'''
    try:
        fout   = open('my_log.txt', 'at')
        size   = len(text) # how many characters in total
        offset = 0
        chunk  = 24
        while True:
            if offset > size:
                # we might choose to termitate our output with a new line character
                fout.write('\n')
                break
            else:
                fout.write(text[offset:offset+chunk]) # [start:stop-before:step]
                offset+=chunk
    except FileExistsError as err:
        print(f'The file already exists {err}')
    except Exception as err: # typically we have several exception handlers for different exceptions
        print(err)
    finally: # this will always run
        pass

# read back
def readFromFile():
    '''declare a file access object to read back text'''
    # we ought to use try-except block here...
    fin = open('my_log.txt', 'r') # 'r' lets us read (text is the default)
    received = fin.read() # just read the whole lot back
    print(received)
    fin.close()

# seek within a text file
def seekContent():
    '''use file access objeect to seek content in a text file'''
    # again, we ought to try-except
    fin = open('my_log.txt', 'rt')
    part = fin.readline()
    print(f'first we read {part}')
    # next we will seek just a few characters
    fin.seek(24) # not common but sometimes useful
    the_rest = fin.read() # from the seek point to the end
    print(f'the rest is {the_rest}')
    fin.close()


if __name__ == '__main__':
    writeToFile('we can persist long strings of characters in a text file')
    readFromFile()
    seekContent()