import socket

# Create a regular socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the payload
payload = b'Hello, This is a test message!'

s.sendto(payload, ('127.0.0.1', 1234))

print(payload)
