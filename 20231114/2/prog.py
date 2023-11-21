class Num:

    def __set__(self, obj, val):
        try:
            obj._val = val.real
        except AttributeError:
            obj._val = len(val)

    def __get__(self, obj, cls):
        try:
            return obj._val
        except AttributeError:
            return 0


import sys
exec(sys.stdin.read())

