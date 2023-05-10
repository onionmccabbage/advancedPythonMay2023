# The majority of computer files are not human readable - they are byte files
def makeBytes(values):
    # lets make some bytes
    b = bytes( values ) 
    print(b) # print will nicely format the bytes as text
    return b

def writeBytes(b):
    # persist these bytes into a file
    try:
        fout = open('bfile', 'wb') # 'w' will (over)write, 'b' for bytes
        fout.write(b)
        fout.close()
    except FileExistsError as err:
        print(f'File already exists {err}')
    except Exception as err:
        print(f'something went wrong {err}')

def readBytes():
    # read bytes back in
    fin = open('bfile', 'rb') # 'rb' will read bytes
    retrieved_b = fin.read()
    fin.close()
    print(retrieved_b)

if __name__ == '__main__':
    values = range(0,256)
    b = makeBytes(values)
    writeBytes(b)
    readBytes()