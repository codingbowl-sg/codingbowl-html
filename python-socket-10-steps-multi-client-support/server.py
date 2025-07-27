import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    if data:
        print(f"Received from {addr}: {data.decode()}")
        conn.sendall(b"Hello from server!")
    conn.close()

HOST = '127.0.0.1'
PORT = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server listening...")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()