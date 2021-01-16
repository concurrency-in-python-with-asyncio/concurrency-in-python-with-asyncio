import asyncpg
import asyncio


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')
    async with connection.transaction():
        query = 'SELECT product_id, product_name from product'
        cursor = await connection.cursor(query) #A
        await cursor.forward(500) #B
        products = await cursor.fetch(100) #C
        for product in products:
            print(product)

    await connection.close()


asyncio.run(main())
