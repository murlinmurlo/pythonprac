from string import ascii_lowercase

class Alpha:
    __slots__ = tuple(ascii_lowercase)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self.__slots__:
                raise AttributeError(f"Invalid attribute: {key}")
            setattr(self, key, value)

    def __str__(self):
        fields = []
        for letter in sorted(self.__slots__):
            if hasattr(self, letter):
                fields.append(f"{letter}: {getattr(self, letter)}")
        return ", ".join(fields)


class AlphaQ:
    __slots__ = tuple(ascii_lowercase)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattribute__(self, name):
        if name in set(ascii_lowercase):
            return object.__getattribute__(self, name)
        else:
            raise AttributeError(f"Invalid attribute: {name}")

    def __setattr__(self, name, value):
        if name in set(ascii_lowercase):
            object.__setattr__(self, name, value)
        else:
            raise AttributeError(f"Invalid attribute: {name}")

    def __str__(self):
        fields = []
        for letter in sorted(ascii_lowercase):
            if hasattr(self, letter):
                fields.append(f"{letter}: {getattr(self, letter)}")
        return ", ".join(fields)




alp = Alpha(c=10, z=2, a=42)
alp.e = 123
print(alp)
alq = AlphaQ(c=10, z=2, a=42)
alq.e = 123
print(alq)

