import asyncio
from util import delay


async def main():
    while True:
        delay_time = input('Enter a time to sleep:')
        asyncio.create_task(delay(int(delay_time)))


asyncio.run(main())
