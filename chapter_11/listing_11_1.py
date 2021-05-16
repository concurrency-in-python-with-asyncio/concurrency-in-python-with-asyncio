import asyncio

counter: int = 0


async def increment():
    global counter
    await asyncio.sleep(0.01)
    counter = counter + 1


async def main():
    global counter
    for _ in range(1000):
        tasks = [asyncio.create_task(increment()) for _ in range(100)]
        await asyncio.gather(*tasks)
        print(f'Counter is {counter}')
        assert counter == 100
        counter = 0


asyncio.run(main())
