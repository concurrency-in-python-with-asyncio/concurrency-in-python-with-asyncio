import asyncpg
import asyncio

async def main():
    connection = await asyncpg.connect(host='0.0.0.0',
                                       port=5432,
                                       user='postgres',
                                       database='postgres',
                                       password='password')
    version = connection.get_server_version()
    print(f'Connected! Postgres version is {version}')
    await connection.close()

asyncio.run(main())
