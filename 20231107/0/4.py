class A: pass
class B: pass
class C(A, B): pass
class D(B, A): pass

class E(D, C): pass

# AC BC - поменять порядок; DC CD  
