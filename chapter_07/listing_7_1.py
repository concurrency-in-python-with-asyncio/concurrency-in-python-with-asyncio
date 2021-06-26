from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


def echo(client: socket):
    while True:
        data = client.recv(2048)
        print(f'Received {data}, sending!')
        client.sendall(data)


with socket(AF_INET, SOCK_STREAM) as server:
    server.bind(('127.0.0.1', 8000))
    server.listen()
    while True:
        connection, _ = server.accept() #A
        thread = Thread(target=echo, args=(connection,)) #B
        thread.start() #C
