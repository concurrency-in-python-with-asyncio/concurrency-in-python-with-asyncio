def positive_integers(until: int):
    for integer in range(until):
        yield integer


positive_iterator = positive_integers(2)

print(next(positive_iterator))
print(next(positive_iterator))
