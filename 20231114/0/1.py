def debug(fun):
    def wrap(*args):
        print("<", args)
        res = fun(*args)
        print(">", res)
        return res
    return wrap

@debug
def mult(a, b):
    '''this is mult'''
    return a*b

res = mult(3, 4)
print(res)

print(help(mult))
