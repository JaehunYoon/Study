import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(('127.0.0.1', 2000))

server_sock.listen(0)

client_sock, addr = server_sock.accept()

data = client_sock.recv(65535)
print('recv : ', data)
client_sock.send(data)

server_sock.close()
client_sock.close()
