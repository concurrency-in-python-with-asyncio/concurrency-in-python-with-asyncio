import asyncio
from util import delay


def call_later():
    print("I'm being called in the future!")


async def main():
    loop = asyncio.get_event_loop()
    loop.call_soon(call_later)
    await delay(1)


asyncio.run(main())
