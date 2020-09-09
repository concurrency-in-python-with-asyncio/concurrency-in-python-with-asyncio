import asyncio


async def main():
    await asyncio.sleep(1)


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
