from itertools import repeat

def travel(n):
    yield from repeat('woo hoo')
    return('bam')

def t(n):
    res = yield from travel(n)
    return('bam bam')

print((t(5))
