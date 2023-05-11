import socket # this provides all we need for socket programming (microservices)

# we can build a socket server
def server():
    '''This microservice will listen for requests on a port and respond'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # these are sensible settings
    # we need some port settings
    port_t = ('localhost', 9874) # choose suitable values
    # bind to these parameters
    server.bind(port_t)
    server.listen() # we need our server to accept requests
    print(f'Server is running on {port_t[0]} port {port_t[1]}')
    # we need a run loop
    while True:
        (client, addr) = server.accept() # unpack any request into the client and address
        # read the first 1024 bytes from the client request
        buf = client.recv(1024) # here we receive bytes
        print(f'Server has received {buf}')
        # we can choose to send a responseto the client
        client.send( buf.upper() ) # send it back in upper case
        client.close() # end of interaction with this client request
        # if the client sends the byte 'quit' then close the server
        if buf == b'quit': # a byte-encoded string
            print('Server is closing')
            server.close() # the ser er stops running
            break

if __name__ == '__main__':
    server()