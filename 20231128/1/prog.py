class dump(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                attrs[attr_name] = cls.wrap_method(attr_name, attr_value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def wrap_method(name, method):
        def wrapped_method(*args, **kwargs):
            filtered_args = tuple(arg for arg in args if isinstance(arg, (str, int, float, bool))) 
            print(f"{name}: {filtered_args}, {kwargs}")
            return method(*args, **kwargs)
        return wrapped_method

import sys
exec(sys.stdin.read())

