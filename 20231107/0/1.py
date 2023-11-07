class A:
    v = 1

class B(A):
    v = 2
    
b = B()
b.v = 3
del b.v
del B.v

print(b.v)
