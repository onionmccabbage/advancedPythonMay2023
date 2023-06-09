import socket # this provides all we need for socket programming (microservices)
from datetime import datetime

# we can build a socket server
def server():
    '''This microservice will listen for requests on a port and respond'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # these are sensible settings
    # we need some port settings
    port_t = ('localhost', 9874) # choose suitable values
    # bind to these parameters
    server.bind(port_t)
    # we can specify how many clients we will allow at once
    # NB this might mean we need to run additional threads in our server
    # then the server will respond to new clients more rapidly
    server.listen(4) # we need our server to accept requests
    print(f'Server is running on {port_t[0]} port {port_t[1]}')
    # we need a run loop
    while True:
        (client, addr) = server.accept() # unpack any request into the client and address
        # read the first 1024 bytes from the client request
        buf = client.recv(1024) # here we receive bytes
        print(f'Server has received {buf}')
        # we can choose to send a response to the client
        # if the client sends the byte 'quit' then close the server
        if buf == b'quit': # a byte-encoded string
            print('Server is closing')
            server.close() # the server stops running
            client.close() # end of interaction with this client request
            break
        # if the client sends b'time' echo back the date and time from the server
        if buf == b'time':
            dt = datetime.today()
            print(f'Server says the time is {dt}')
            client.send(str(dt).encode())
        client.send( buf.upper() ) # send it back in upper case
        client.close() # end of interaction with this client request


if __name__ == '__main__':
    server()