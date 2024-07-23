import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.49.65',8080)

client_socket.connect(server_address)
print("Connected to Server !")

while True:
    message = input("Client :")
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024)
    print("Received from server:", response.decode())

client_socket.close()