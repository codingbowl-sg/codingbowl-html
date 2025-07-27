# client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

client.send("Hi Server!".encode())
response = client.recv(1024).decode()
print(f"Server says: {response}")

client.close()
