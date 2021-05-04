import socket

HOST = '127.0.0.1'
PORT = 7777

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect((HOST, PORT))
socket_cliente.sendall(str.encode("oi"))

data = socket_cliente.recv(1024)
print("mensagem q vorto: ", data.decode())