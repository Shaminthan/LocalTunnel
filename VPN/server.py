# server.py
import socket
import ssl

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4443))
server_socket.listen(5)
print("VPN Server listening on port 4443...")

# Wrap with SSL
# Wrap with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
context.verify_mode = ssl.CERT_NONE  # Add here to skip client cert validation

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    secure_socket = context.wrap_socket(client_socket, server_side=True)

    try:
        while True:
            data = secure_socket.recv(4096)
            if not data:
                break
            print("Received:", data.decode())
            secure_socket.sendall(b"Data received securely!")
    except:
        pass
    secure_socket.close()
