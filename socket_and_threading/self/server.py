# import socket
# from _thread import start_new_thread
# import threading

# lock = threading.Lock()

# def handle_client(c):
#     while True:
#         data = c.recv(1024)
#         if not data:
#             print('Bye')
#             lock.release()
#             break
#         c.send(data[::-1])
#     c.close()

# def main():
#     host = ''
#     port = 12345
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
#     s.bind((host, port))
#     s.listen(5)
#     print("Server running on port", port)

#     while True:
#         c, addr = s.accept()
#         lock.acquire()
#         print('Connected to:', addr[0], ':', addr[1])
#         start_new_thread(handle_client, (c,))

# if __name__ == '__main__':
#     main()

import socket
from _thread import start_new_thread
import threading

host = '100.81.1.108'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket with IPv4 and port 
clients = []

def handle_client(c, addr):
    while True:
        try:
            data = c.recv(1024)
            if not data:
                break
                
            # broadcast to all client
            if c in clients:
                if clients != c:
                    clients.send(f"{addr[0]}:{addr[1]} say: {data.decode('ascii')}".encode('ascii'))
        except:
            break

    c.close() # shutdown the process
    clients.remove(c)
    print(f"Disconnect: {addr[0]}:{addr[1]}")

def main():
    # set host and port for our server
    s.bind((host, port)) # this bind is like we assign the host and port to the server
    s.listen(5)
    print(f"Server running on port {port}")

    while True:
        c, addr = s.accept()
        clients.append(c)
        print(f"Connected to: {addr[0]} : {addr[1]}")
        data = c.recv(1024).decode('ascii')
        print(data)
        r = 'Received'
        c.send(r.encode())
        start_new_thread(handle_client, (c, addr))

if __name__ == '__main__':
    main()