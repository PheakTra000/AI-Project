#import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

def main():
    # creating a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connect to server on {HOST} {PORT}")
    except:
        print(f"Unable to connect to the server {HOST} {PORT}")
if __name__ == '__main__':
    main()
