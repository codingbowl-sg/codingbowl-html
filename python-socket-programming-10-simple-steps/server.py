# server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

print("Server is listening on port 5555...")

client_socket, address = server.accept()
print(f"Connected to {address}")

data = client_socket.recv(1024).decode()
print(f"Client says: {data}")

client_socket.send("Hello from server!".encode())
client_socket.close()
