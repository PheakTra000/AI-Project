import socket
import threading

HOST = '100.81.1.108'
PORT = 1234 # we can use any port from 0 to 65535
LISTENER_LIMIT = 5
active_clients = [] #list of all currently connected users

#function to listen for upcoming messages from a client
def listen_for_messages(client, username):
    while True:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + ': ' + message
            send_messages_to_all(final_msg)
        else:
            print(f"The message send from client {username} is empty")

#function to send the message to a single client
def send_messages_to_client(client, message):
    client.sendall(message.encode())

# function to send message to all client that are currently connected to this server
def send_messages_to_all(from_username, message):
    for user in active_clients:
        send_messages_to_client(user[1], message)


#function to hand client
def client_handler(client):

    # server will listen for client message that will contain the username
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
        else:
            print("Client name is empty")
    threading.Thread(target=listen_for_messages, args=(client, username, )).start()

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

        threading.Thread(target=client_handler, args=(client, )).start()



if __name__ == '__main__':
    main()
