import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
clients = []
usernames = {}

def broadcast(message, sender_socket=None):
    """Send a message to all clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    """Handle communication with a single client."""
    try:
        username = client_socket.recv(1024).decode()
        usernames[client_socket] = username
        welcome_message = f"{username} has joined the chat."
        broadcast(welcome_message.encode(), client_socket)
        print(welcome_message)

        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            formatted_message = f"{username}: {message.decode()}"
            broadcast(formatted_message.encode(), client_socket)
            print(formatted_message)
    except:
        pass
    finally:
        if client_socket in clients:
            clients.remove(client_socket)
        left_message = f"{usernames.get(client_socket, 'A user')} has left the chat."
        broadcast(left_message.encode(), client_socket)
        print(left_message)
        client_socket.close()
        usernames.pop(client_socket, None)

def main():
    """Start the server and accept client connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server started on {HOST}:{PORT}...")
    while True:
        client_socket, addr = server.accept()
        print(f"Connected to {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

if __name__ == "__main__":
    main()