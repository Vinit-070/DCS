import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.49.65', 8080)

server_socket.bind(server_address)

server_socket.listen(1)
print("Server is listening on", server_address)

connection, client_address = server_socket.accept()
print("Connected by", client_address)

while True:
    data = connection.recv(1024)
    if not data:
        break
    print("Received from client:", data.decode())


    response = "Server response: " + data.decode()
    connection.sendall(response.encode())

connection.close()