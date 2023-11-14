def repeat(n):
    def repeater(fun):
        def newfun(*args, **kwargs):
            res = fun(*args, **kwargs)
            return n*[res]
        return newfun
    return repeater

@repeat(4)
def mult(a, b):
    return(a*b)

res = mult(3, 4)
print(res)

