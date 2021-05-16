async def say_hello():
    print('Hello!')


async def say_goodbye():
    print('Goodbye!')


async def meet_and_greet():
    await say_hello()
    await say_goodbye()


coro = meet_and_greet()

coro.send(None)
