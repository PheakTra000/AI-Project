import socket
import threading

HOST = '100.81.1.108'
PORT = 1234 # we can use any port from 0 to 65535
LISTENER_LIMIT = 5

def main():
    # creating the socket class object
    # AF_INET: we are going to use IPv4 address
    # SOCK_STERAM: using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # creating a try catch block
    try:
        # provide the server with an address in the form of host ip and port
        server.bind((HOST, PORT))
        print(f"Running this server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # set server limit
    server.listen(LISTENER_LIMIT)

    # this while loop will keep listening to client connections
    while True:

        client, address = server.accept()
        print(f"Successfully connected to client{address[0]} {address[1]}")

if __name__ == '__main__':
    main()
