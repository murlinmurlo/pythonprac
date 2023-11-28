class final(type):
    def __new__(metacls, name, parents, namespace):
        for cls in parents:
            if isinstance(cls, final):
                raise TypeError(f"{cls.__name__} is final")
        return super().__new__(metacls, name, parents, namespace)
class E(metaclass=final): pass
class C: pass
class A(C, E): pass



class sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError("Class can only have one direct parent")
        return super().__new__(metacls, name, parents, namespace)

class E(metaclass=sole):
    pass

class C:
    pass

class A(C, E):
    pass
