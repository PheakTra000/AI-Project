import socket
import threading

HOST = '100.81.1.108'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = []  # list of (username, client_socket)

def listen_for_messages(client, username):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                final_msg = f"{username}: {message}"
                send_messages_to_all(final_msg)
            else:
                print(f"Client {username} disconnected")
                remove_client(client)
                break
        except:
            print(f"Connection with {username} lost")
            remove_client(client)
            break

def send_messages_to_client(client, message):
    try:
        client.sendall(message.encode())
    except:
        remove_client(client)

def send_messages_to_all(message):
    for username, client in active_clients:
        send_messages_to_client(client, message)

def remove_client(client):
    for user in active_clients:
        if user[1] == client:
            active_clients.remove(user)
            break
    client.close()

def client_handler(client):
    try:
        username = client.recv(2048).decode('utf-8')
        if username:
            active_clients.append((username, client))
            print(f"{username} joined the chat")
            threading.Thread(target=listen_for_messages, args=(client, username), daemon=True).start()
        else:
            client.close()
    except:
        client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print(f"Running server on {HOST}:{PORT}")
    except:
        print(f"Unable to bind to {HOST}:{PORT}")
        return

    server.listen(LISTENER_LIMIT)
    print("Server is listening...")

    while True:
        client, address = server.accept()
        print(f"Connected to client {address[0]}:{address[1]}")
        threading.Thread(target=client_handler, args=(client,), daemon=True).start()

if __name__ == '__main__':
    main()
