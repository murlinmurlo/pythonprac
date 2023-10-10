from decimal import Decimal as d

def factorial(m):
    mul = 1
    for i in range(1, m+1):
        mul *= i
    return mul

def esum(N, one):
    _sum = d(0)  
    for n in range(N):
        _sum += d(1) / factorial(n)
    return _sum

print(esum(100, d(1)))
