def calc(n):
    s = 0
    while n:
        s += n
        yield n
        n //= 2
    return s

print(list(calc(17)))


def runner(n):
    res = yield from calc(n)
    yield res

list(runner(25))
