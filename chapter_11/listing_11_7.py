import asyncio
from asyncio import Semaphore
from aiohttp import ClientSession


async def get_url(url: str,
                  session: ClientSession,
                  semaphore: Semaphore):
    print('Waiting to acquire semaphore...')
    async with semaphore:
        print('Acquired semaphore, requesting...')
        response = await session.get(url)
        print('Finished requesting')
        return response.status


async def main():
    semaphore = Semaphore(10)
    async with ClientSession() as session:
        tasks = [get_url('http://www.example.com', session, semaphore) for _ in range(1000)]
        await asyncio.gather(*tasks)


asyncio.run(main())
