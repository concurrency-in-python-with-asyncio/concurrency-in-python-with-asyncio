import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Finished counting to {count_to} in {end-start}')
    return counter


if __name__ == "__main__":
    start_time = time.time()

    from_one_hundred_million = Process(target=count, args=(100000000,))
    from_two_hundred_million = Process(target=count, args=(200000000,))

    from_one_hundred_million.start()
    from_two_hundred_million.start()

    from_one_hundred_million.join()
    from_two_hundred_million.join()

    end_time = time.time()
    print(f'Completed in {end_time-start_time}')
