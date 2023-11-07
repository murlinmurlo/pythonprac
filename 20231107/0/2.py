class A:
    def __init__(self, var):
        self.var = var

    def __add__(self, num):
        return self.__class__(self.var + num)

a = A(1)


class B(A):
    def __str__(self):
        return f"<{self.var}>"

a = B(12)
print(a+1)
