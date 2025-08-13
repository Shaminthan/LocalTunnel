# client.py
import socket
import ssl

# Create SSL context that does NOT verify certificates
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Connect to server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_sock = context.wrap_socket(sock, server_hostname="localhost")

secure_sock.connect(('127.0.0.1', 4443))

secure_sock.sendall(b"Hello from VPN client!")
print("Server replied:", secure_sock.recv(4096).decode())

secure_sock.close()
