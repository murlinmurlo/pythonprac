from itertools import *

def slide(seq, n):
    for el in range(len(seq)):
        yield from islice(seq, el, el + n)

import sys
exec(sys.stdin.read())


