import string


class Alpha:
    __slots__ = list(string.ascii_lowercase)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __str__(self):
        string_list = [f"{slot}: {getattr(self, slot)}"
             for slot in self.__slots__ if hasattr(self, slot)]
        return ", ".join(string_list)


class AlphaQ:
    __slots__ = frozenset(string.ascii_lowercase)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if key not in self.__slots__:
                raise AttributeError
            setattr(self, key, val)

    def __setattr__(self, key, val):
        if key not in self.__slots__:
            raise AttributeError
        super().__setattr__(key, val)

    def __str__(self):
        string_list = [f"{key}: {getattr(self, key)}" for key in sorted(self.__slots__) if hasattr(self, key)]
        return ", ".join(string_list)


import sys
exec(sys.stdin.read())


