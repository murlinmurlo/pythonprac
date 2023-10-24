import itertools

def f():
    yield from itertools.product(range(1, 8), 'ABCDEGFH')

print(list(f()))
