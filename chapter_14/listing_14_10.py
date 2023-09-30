import functools
import selectors
import socket
from listing_14_8 import CustomFuture
from selectors import BaseSelector


def accept_connection(future: CustomFuture, connection: socket.socket): #A
    print(f'We got a connection from {connection}!')
    future.set_result(connection)


async def sock_accept(sel: BaseSelector, sock) -> socket.socket: #B
    print('Registering socket to listen for connections')
    future = CustomFuture()
    sel.register(sock, selectors.EVENT_READ, functools.partial(accept_connection, future))
    print('Pausing to listen for connections...')
    connection: socket.socket = await future
    return connection


async def main(sel: BaseSelector):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('127.0.0.1', 8000))
    sock.listen()
    sock.setblocking(False)

    print('Waiting for socket connection!')
    connection = await sock_accept(sel, sock) #C
    print(f'Got a connection {connection}!')


selector = selectors.DefaultSelector()

coro = main(selector)

while True: #D
    try:
        state = coro.send(None)

        events = selector.select()

        for key, mask in events:
            print('Processing selector events...')
            callback = key.data
            callback(key.fileobj)
    except StopIteration as si:
        print('Application finished!')
        break
