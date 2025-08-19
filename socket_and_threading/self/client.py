# import socket

# def main():
#     host = '127.0.0.1'
#     port = 12345

#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((host, port))

#     msg = "hello from client"
#     while True:
#         s.send(msg.encode('ascii'))
#         data = s.recv(1024)
#         print('Received from server:', data.decode('ascii'))

#         ans = input('Do you want to continue (y/n): ')
#         if ans.lower() != 'y':
#             break

#     s.close()

# if __name__ == '__main__':
#     main()

import socket
import threading

host = '100.81.1.108'
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_message(m):
    s.send(m.encode())
    data = ''
    data = s.recv(1024).decode('ascii')
    print(data)

def receive_message():
    while True:
        try:
            data = s.recv(1024).decode('ascii')
            if data:
                print(f'\n{data}')
        except:
            break



def main():
    s.connect((host, port))

    msg = "Hello from client"

    threading.Thread(target=receive_message, daemon=True).start()
    while True:
        s.send(msg.encode('ascii'))
        data = s.recv(1024)
        print(f'Receive from server: {data.decode('ascii')}')

        ans = input('Do you want to continue (y/n): ')
        if ans.lower() == 'y':
            while True:
                m = input("Enter: ")
                send_message(m)
                
        s.close()

if __name__ == '__main__':
    main()