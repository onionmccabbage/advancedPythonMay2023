import socket
import sys

def client():
    '''This is a basic socket client to interact with the server'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # match the server
    port_t = ('localhost', 9874)
    sock.connect( port_t ) # we connect to the server
    message='client says hello'
    sock.send( message.encode() ) # we must always encode any string of data
    # we handle any response from the server
    data = sock.recv(1024) # read up to 1024 bytes
    print(f'Client received {data}')
    sock.close()

if __name__ == '__main__':
    client()