import asyncio
from enum import Enum


class ConnectionState(Enum):
    WAIT_INIT = 0
    INITIALIZING = 1
    INITIALIZED = 2


class Connection:

    def __init__(self):
        self.state = ConnectionState.WAIT_INIT
        self.condition = asyncio.Condition()

    async def change_state(self, state: ConnectionState):
        async with self.condition:
            print(f'change_state: State changing from {self.state} to {state}')
            self.state = state
            self.condition.notify_all()

    async def initialize(self):
        await self.change_state(ConnectionState.INITIALIZING)
        print('initialize: Initializing connection...')
        await asyncio.sleep(3)  # simulate connection startup time
        print('initialize: Finished initializing connection')
        await self.change_state(ConnectionState.INITIALIZED)

    async def execute(self, query: str):
        async with self.condition:
            print('execute: Waiting for connection to initialize')
            await self.condition.wait_for(self._is_initialized)
            print(f'execute: Running {query}!!!')
            await asyncio.sleep(3)  # simulate a long query

    def _is_initialized(self):
        if self.state is not ConnectionState.INITIALIZED:
            print(f'_is_initialized: Connection not finished initializing, state is {self.state}')
            return False
        print(f'_is_initialized: Connection is initialized!')
        return True


async def main():
    connection = Connection()
    query_one = asyncio.create_task(connection.execute('select * from table'))
    query_two = asyncio.create_task(connection.execute('select * from other_table'))
    asyncio.create_task(connection.initialize())
    await query_one
    await query_two


asyncio.run(main())
