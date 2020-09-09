import asyncio
from util import delay


async def hello_every_second():
    for i in range(3):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting!")


async def main():
    first_delay = asyncio.create_task(delay(4))
    second_delay = asyncio.create_task(delay(4))
    await hello_every_second()
    await first_delay
    await second_delay

asyncio.run(main())