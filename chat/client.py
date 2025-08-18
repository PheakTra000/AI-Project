#import required modules
import socket
import threading

HOST = '100.81.1.108'
PORT = 1234


def listen_for_messages_from_server(client):
    while True:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split(":")[0]
            content = message.message.split(':')[1]

            print(f"[{username}] {content}")
        else:
            print("Message received from client is empty")

def send_message_to_server(client):
    while True:
        message = input("Message: ")
        if message != '':
            client.sendall(message.encode())
        else:
            print("empty message")
            exit(0)

def communicate_to_server(client):
    username = input("Enter username: ")
    if username != '':
        client.sendall(username.encode())
    else:
        print("Username cannot be empty")
        exit(0)

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    send_message_to_server(client)

def main():
    # creating a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connect to server on {HOST} {PORT}")
    except:
        print(f"Unable to connect to the server {HOST} {PORT}")

    communicate_to_server(client)
if __name__ == '__main__':
    main()
