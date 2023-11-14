def debug(fun):
    def wrap(*args):
        for i in args:
            if type(i) != int:
                raise TypeError("not float")
    return wrap

@debug
def mult(a, b):
    '''this is mult'''
    return a*b

res = mult(3.4, "nanana")
print(res)

print(help(mult))
