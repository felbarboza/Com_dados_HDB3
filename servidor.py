import socket

HOST = 'localhost'
PORT = 7777


if __name__ == "__main__": 
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
    
def startSv(host, port):
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind((HOST, PORT))
    socket_server.listen()
    print("Aguardando cliente")

def listen(interval):
  socket_server.settimeout(interval)
  conn, address = socket_server.accept()
  
  print("Conectado em ", address)
  
  while True:
    data = conn.recv(1024)
    if not data:
      print("Message ended.")
      conn.close()
      break
    print(data.decode())
    return data
    conn.sendall(data)