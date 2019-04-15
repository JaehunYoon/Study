import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 2000))

sock.send('hello'.encode())
data = sock.recv(65535)

print(data.decode())

sock.close()
