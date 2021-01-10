import asyncio


async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 250


asyncio.run(main(), debug=True)
