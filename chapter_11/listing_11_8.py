import asyncio
from asyncio import Semaphore


async def acquire(semaphore: Semaphore):
    print('Waiting to acquire')
    async with semaphore:
        print('Acquired')
        await asyncio.sleep(5)
    print('Releasing')


async def release(semaphore: Semaphore):
    print('Releasing as a one off!')
    semaphore.release()
    print('Released as a one off!')


async def main():
    semaphore = Semaphore(2)

    print("Acquiring twice, releasing three times...")
    await asyncio.gather(acquire(semaphore),
                         acquire(semaphore),
                         release(semaphore))

    print("Acquiring three times...")
    await asyncio.gather(acquire(semaphore),
                         acquire(semaphore),
                         acquire(semaphore))


asyncio.run(main())
