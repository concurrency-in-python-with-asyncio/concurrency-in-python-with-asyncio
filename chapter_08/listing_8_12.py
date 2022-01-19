import asyncio
import logging
from asyncio import StreamReader, StreamWriter


class ServerState:

    def __init__(self):
        self._writers = []

    async def add_client(self, reader: StreamReader, writer: StreamWriter): #A
        self._writers.append(writer)
        await self._on_connect(writer)
        asyncio.create_task(self._echo(reader, writer))

    async def _on_connect(self, writer: StreamWriter): #B
        writer.write(f'Welcome! {len(self._writers)} user(s) are online!\n'.encode())
        await writer.drain()
        await self._notify_all('New user connected!\n')

    async def _echo(self, reader: StreamReader, writer: StreamWriter): #C
        try:
            while (data := await reader.readline()) != b'':
                writer.write(data)
                await writer.drain()
            self._writers.remove(writer)
            await self._notify_all(f'Client disconnected. {len(self._writers)} user(s) are online!\n')
        except Exception as e:
            logging.exception('Error reading from client.', exc_info=e)
            self._writers.remove(writer)

    async def _notify_all(self, message: str): #D
        for writer in self._writers:
            try:
                writer.write(message.encode())
                await writer.drain()
            except ConnectionError as e:
                logging.exception('Could not write to client.', exc_info=e)
                self._writers.remove(writer)


async def main():
    server_state = ServerState()

    async def client_connected(reader: StreamReader, writer: StreamWriter) -> None: #E
        await server_state.add_client(reader, writer)

    server = await asyncio.start_server(client_connected, '127.0.0.1', 8000) #F

    async with server:
        await server.serve_forever()


asyncio.run(main())
