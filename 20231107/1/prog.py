import collections

class DivStr(collections.UserString):
    def __init__(self, data = ''):
        super().__init__(data)

    def __floordiv__(self, other):
        for i in range(other):
            yield self.__class__(self[i * (len(self) // other):(i + 1) * (len(self) // other)])
    
    def __mod__(self, other):
        if len(self) % other:
            return self.__class__(self[-(len(self) % other):])
        else:
            return self.__class__('')

import sys
exec(sys.stdin.read())
