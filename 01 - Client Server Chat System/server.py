import socket
import threading

def handle_receive(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("👂 Client:", data.decode())

def handle_send(conn):
    while True:
        msg = input("You: ")
        conn.send(msg.encode())

# Setup server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("🚀 Waiting for connection...")

conn, addr = server_socket.accept()
print(f"✅ Connected to {addr}")

# Start receiving and sending in parallel
threading.Thread(target=handle_receive, args=(conn,), daemon=True).start()
handle_send(conn)
