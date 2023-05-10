# we can read and write text, byte etc with persistent files
# Python provides file access objects for this

# write text (defaults to text)
fout = open('snip.txt', 'at') # 'a' will append, 'w' will (over)write, 'x' for exclusive access
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
                break
            else:
                fout.write(text[offset:offset+chunk]) # [start:stop-before:step]
                offset+=chunk
    except Exception as err: # typically we have several exception handlers for different exceptions
        print(err)
    finally: # this will always run
        pass

if __name__ == '__main__':
    writeToFile('we can persist long strings of characters in a text file')