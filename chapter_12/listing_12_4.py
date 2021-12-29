import asyncio
import aiohttp
import logging
from asyncio import Queue
from aiohttp import ClientSession
from bs4 import BeautifulSoup


class WorkItem:
    def __init__(self, item_depth: int, url: str):
        self.item_depth = item_depth
        self.url = url


async def worker(worker_id: int, queue: Queue, session: ClientSession, max_depth: int):
    print(f'Worker {worker_id}')
    while True: #A
        work_item: WorkItem = await queue.get()
        print(f'Worker {worker_id}: Processing {work_item.url}')
        await process_page(work_item, queue, session, max_depth)
        print(f'Worker {worker_id}: Finished {work_item.url}')
        queue.task_done()


async def process_page(work_item: WorkItem, queue: Queue, session: ClientSession, max_depth: int): #B
    try:
        response = await asyncio.wait_for(session.get(work_item.url), timeout=3)
        if work_item.item_depth == max_depth:
            print(f'Max depth reached, '
                  f'not processing more for {work_item.url}')
        else:
            body = await response.text()
            soup = BeautifulSoup(body, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                queue.put_nowait(WorkItem(work_item.item_depth + 1,
                                          link['href']))
    except Exception as e:
        logging.exception(f'Error processing url {work_item.url}')


async def main(): #C
    start_url = 'http://example.com'
    url_queue = Queue()
    url_queue.put_nowait(WorkItem(0, start_url))
    async with aiohttp.ClientSession() as session:
        workers = [asyncio.create_task(worker(i, url_queue, session, 3))
                   for i in range(100)]
        await url_queue.join()
        [w.cancel() for w in workers]


asyncio.run(main())
