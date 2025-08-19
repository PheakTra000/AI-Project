import socket
import threading

HOST = '100.69.34.80'
PORT = 1234

def listen_for_messages_from_server(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                if ":" in message:
                    username, content = message.split(":", 1)
                    print(f"[{username}] {content}")
                else:
                    print(f"[Server] {message}")
            else:
                print("Message received from server is empty")
                break
        except:
            print("Connection to server lost")
            break

def send_message_to_server(client):
    while True:
        try:
            message = input("Message: ")
            if message.strip():
                client.sendall(message.encode())
            else:
                print("Empty message not sent")
        except:
            print("Connection closed")
            client.close()
            break

def communicate_to_server(client):
    username = input("Enter username: ")
    if username.strip():
        client.sendall(username.encode())
    else:
        print("Username cannot be empty")
        client.close()
        return

    threading.Thread(target=listen_for_messages_from_server, args=(client,), daemon=True).start()
    send_message_to_server(client)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connected to server on {HOST}:{PORT}")
    except:
        print(f"Unable to connect to server {HOST}:{PORT}")
        return

    communicate_to_server(client)

if __name__ == '__main__':
    main()
