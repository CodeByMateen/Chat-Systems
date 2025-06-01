import socket
import threading

def handle_receive(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print("👂 Server:", data.decode())

def handle_send(sock):
    while True:
        msg = input("You: ")
        sock.send(msg.encode())

# Setup client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
print("🔗 Connected to server")

# Start receiving and sending in parallel
threading.Thread(target=handle_receive, args=(client_socket,), daemon=True).start()
handle_send(client_socket)
