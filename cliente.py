import socket

HOST = '127.0.0.1'
PORT = 7777

DATA_TESTE_RECEBIDO = ['0', '0', '+', '-', '0', '0', '+', '0', '0', '0', '-', '+', '0', '0', '-', '0', '0', '0', '+', '-', '0', '0', '+', '0', '0', '0', '-', '+', '0', '0', '-', '0', '0', '0', '+', '-', '0', '0', '0', '+', '0', '0', '-', '+', '0', '-', '+', '0'] 


def listToString(list):
    str1 = ""
    return (str1.join(list))


if __name__ == "__main__": 
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((HOST, PORT))
    socket_cliente.sendall(str.encode(listToString(DATA_TESTE_RECEBIDO)))
    

def enviar(port, address, msg):
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((address, port))
    socket_cliente.sendall(str.encode(listToString(msg)))
