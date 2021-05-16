import asyncio
from asyncio import Queue
from random import randrange
from typing import List


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id: int, products: List[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty(): #A
        customer: Customer = queue.get_nowait()
        print(f'Cashier {cashier_number} checking out customer {customer.customer_id}')
        for product in customer.products: #B
            print(f"Cashier {cashier_number} checking out customer {customer.customer_id}'s {product.name}")
            await asyncio.sleep(product.checkout_time)
        print(f'Cashier {cashier_number} finished checking out customer {customer.customer_id}')
        queue.task_done()


async def main():
    customer_queue = Queue()

    all_products = [Product('beer', 2),
                    Product('bananas', .5),
                    Product('sausage', .2),
                    Product('diapers', .2)]

    for i in range(10): #C
        products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
        customer_queue.put_nowait(Customer(i, products))

    cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)] #D

    await asyncio.gather(customer_queue.join(), *cashiers)

asyncio.run(main())
