from typing import Generator


def generator(start: int, end: int):
    for i in range(start, end):
        yield i


one_to_five = generator(1, 5)
five_to_ten = generator(5, 10)


def run_generator_step(gen: Generator[int, None, None]): #A
    try:
        return gen.send(None)
    except StopIteration as si:
        return si.value


while True: #B
    one_to_five_result = run_generator_step(one_to_five)
    five_to_ten_result = run_generator_step(five_to_ten)
    print(one_to_five_result)
    print(five_to_ten_result)

    if one_to_five_result is None and five_to_ten_result is None:
        break
