import socket

HOST = '127.0.0.1'
PORT = 50000

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect((HOST, PORT))
socket_cliente.sendall(str.encode("eae meu parça"))

data = socket_cliente.recv(1024)
print("mensagem q vorto: ", data.decode())