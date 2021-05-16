import asyncio
import functools
from asyncio import Event


def trigger_event(event: Event):
    event.set()


async def do_work_on_event(event: Event):
    print('Waiting for event...')
    await event.wait() #A
    print('Performing work!')
    await asyncio.sleep(1) #B
    print('Finished work!')
    event.clear() #C


async def main():
    event = asyncio.Event()
    asyncio.get_running_loop().call_later(5.0, functools.partial(trigger_event, event)) #D
    await asyncio.gather(do_work_on_event(event), do_work_on_event(event))


asyncio.run(main())
