import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def receive_messages(sock):
    """Receive and print messages from the server."""
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                break
            print(message.decode())
        except:
            break

def main():
    """Connect to the server and handle user input."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    username = input("Enter your username: ")
    client.sendall(username.encode())  # Send username to the server

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    print("Type your messages below. Type 'exit' to disconnect.")
    while True:
        msg = input()
        if msg.lower() == 'exit':
            break
        client.sendall(msg.encode())

    client.close()

if __name__ == "__main__":
    main()