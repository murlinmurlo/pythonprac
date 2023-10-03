'''
def f(x):
    return(2*x)
def g(x):
    return(3*x)

def fun(f, g):
    return(f(x)+ g(x))

print(fun(2))
'''

def addx(a):
    def fun(x):
        return x + a
    return fun

def addx(a):
    return lambda x: a + x
