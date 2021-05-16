import asyncio
from asyncio import StreamWriter, StreamReader
from asyncio.subprocess import Process


async def consume_and_send(text_list, stdout: StreamReader, stdin: StreamWriter):
    for text in text_list:
        line = await stdout.read(2048)
        print(line)
        stdin.write(text.encode())
        await stdin.drain()


async def main():
    program = ['python3', 'listing_13_13.py']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE,
                                                            stdin=asyncio.subprocess.PIPE)

    text_input = ['one\n', 'two\n', 'three\n', 'four\n', 'quit\n']

    await asyncio.gather(consume_and_send(text_input, process.stdout, process.stdin), process.wait())


asyncio.run(main())
