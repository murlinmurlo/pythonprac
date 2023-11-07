class A:
    def __str__(self):
        __f = 35
        return f"{self.__f}"

class   B(A):
    def __init__(self):
        self.__f = 100500


a = A()

print(a)
