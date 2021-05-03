import socket

HOST = '192.168.15.153'
PORT = 50000

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((HOST, PORT))
socket_server.listen()
print("Aguardando cliente")
conn, address = socket_server.accept()

print("Conectado em ", address)

while True:
  data = conn.recv(1024)
  if not data:
    print("Message ended.")
    conn.close()
    break
  print(data.decode())
  conn.sendall(data)