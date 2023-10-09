from math import *

def Calc(s, t, u):
    def s(x):
        return eval(s)
    def t(x):
        return eval(t)
    def u(x, y):
        return eval(u)

    return lambda x: u(s(x), t(x))


print(Calc(*eval(input()))(eval(input())))
