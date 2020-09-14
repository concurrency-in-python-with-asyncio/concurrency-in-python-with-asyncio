import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f'I got a connection from {client_address}!')

    buffer = connection.recv(2)
    print(f'I got data: {buffer}!')

    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)
        print(f'I got data: {data}!')
        buffer = buffer + data

    print(f"All the data is: {buffer}")
finally:
    server_socket.close()
